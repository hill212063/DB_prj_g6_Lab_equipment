from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from Main.models import *
from Main.serializers import *

# Faculty views
@csrf_exempt
def facultyApi(request, id=0):
    if request.method == 'GET':
        faculty = Faculty.objects.all()
        faculty_serializer = FacultySerializer(faculty, many=True)
        return JsonResponse(faculty_serializer.data, safe=False)

    elif request.method == 'POST':
        faculty_data = JSONParser().parse(request)
        faculty_serializer = FacultySerializer(data=faculty_data)

        if faculty_serializer.is_valid():
            faculty_serializer.save()
            return JsonResponse("Added successfully!", safe=False)
        else:
            return JsonResponse("Failed to add.", safe=False)

    elif request.method == 'PUT':
        faculty_data = JSONParser().parse(request)
        faculty = Faculty.objects.get(id=id)
        faculty_serializer = FacultySerializer(faculty, data=faculty_data)

        if faculty_serializer.is_valid():
            faculty_serializer.save()
            return JsonResponse("Updated successfully!", safe=False)
        else:
            return JsonResponse("Failed to update.", safe=False)

    elif request.method == 'DELETE':
        faculty = Faculty.objects.get(id=id)
        faculty.delete()
        return JsonResponse("Deleted successfully!", safe=False)

# Department views
@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        department = Department.objects.all()
        department_serializer = DepartmentSerializer(department, many=True)
        return JsonResponse(department_serializer.data, safe=False)

    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)

        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added successfully!", safe=False)
        else:
            return JsonResponse("Failed to add.", safe=False)

    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Department.objects.get(id=id)
        department_serializer = DepartmentSerializer(department, data=department_data)

        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated successfully!", safe=False)
        else:
            return JsonResponse("Failed to update.", safe=False)

    elif request.method == 'DELETE':
        department = Department.objects.get(id=id)
        department.delete()
        return JsonResponse("Deleted successfully!", safe=False)

# User_privileges API views
@csrf_exempt
def user_privileges_api(request, id=0):
    if request.method == 'GET':
        if id:
            user_privilege = User_privileges.objects.get(id=id)
            user_privilege_serializer = User_privilegesSerializer(user_privilege)
            return JsonResponse(user_privilege_serializer.data)
        else:
            user_privileges = User_privileges.objects.all()
            user_privileges_serializer = User_privilegesSerializer(user_privileges, many=True)
            return JsonResponse(user_privileges_serializer.data, safe=False)

    elif request.method == 'POST':
        user_privilege_data = JSONParser().parse(request)
        user_privilege_serializer = User_privilegesSerializer(data=user_privilege_data)
        if user_privilege_serializer.is_valid():
            user_privilege_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        user_privilege_data = JSONParser().parse(request)
        user_privilege = User_privileges.objects.get(id=id)
        user_privilege_serializer = User_privilegesSerializer(user_privilege, data=user_privilege_data)
        if user_privilege_serializer.is_valid():
            user_privilege_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        user_privilege = User_privileges.objects.get(id=id)
        user_privilege.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)


# User API views
@csrf_exempt
def user_api(request, id=0):
    if request.method == 'GET':
        if id:
            user = User.objects.get(id=id)
            user_serializer = UserSerializer(user)
            return JsonResponse(user_serializer.data)
        else:
            users = User.objects.all()
            user_serializer = UserSerializer(users, many=True)
            return JsonResponse(user_serializer.data, safe=False)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        print(user_serializer)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = User.objects.get(id=id)
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        user = User.objects.get(id=id)
        user.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)
    


from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException , AuthenticationFailed

from .authentication import create_access_token, create_refresh_token , decode_access_token , decode_refresh_token
from .serializers import UserSerializer
from .models import User


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class LoginAPIView(APIView):
    def post(self, request):
        user = User.objects.filter(u_email=request.data['u_email']).first()

        if not user:
            raise APIException('Invalid credentials!')

        if user.u_password != request.data['u_password']:
            raise APIException('Invalid credentials!')
      
        access_token = create_access_token(user.id,str(user.u_privilege))
        refresh_token = create_refresh_token(user.id,str(user.u_privilege))

        response = Response()

        response.set_cookie(key='refreshToken', value=refresh_token, httponly=True)
        response.data = {
            'token': access_token
        }

        return response
    
class UserAPIView(APIView):
    def get(self, request):
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token = auth[1].decode('utf-8')
            id = decode_access_token(token)[0]

            user = User.objects.filter(pk=id).first()

            return Response(UserSerializer(user).data)

        raise AuthenticationFailed('unauthenticated')
    
class RefreshAPIView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refreshToken')
 
        id = decode_refresh_token(refresh_token)[0]
        role = decode_refresh_token(refresh_token)[1]
        access_token = create_access_token(id,role)
        return Response({
            'token': access_token
        })

class LogoutAPIView(APIView):
    def post(self, _):
        response = Response()
        response.delete_cookie(key="refreshToken")
        response.data = {
            'message': 'success'
        }
        return response
    
#Id_types
@csrf_exempt
def Id_typesApi(request, id=0):
    if request.method == 'GET':
        id_types = Id_types.objects.all()
        id_types_serializer = Id_typesSerializer(id_types, many=True)
        return JsonResponse(id_types_serializer.data, safe=False)

    elif request.method == 'POST':
        id_types_data = JSONParser().parse(request)
        id_types_serializer = Id_typesSerializer(data=id_types_data)

        if id_types_serializer.is_valid():
            id_types_serializer.save()
            return JsonResponse("Added successfully!", safe=False)
        else:
            return JsonResponse("Failed to add.", safe=False)

    elif request.method == 'PUT':
        id_types_data = JSONParser().parse(request)
        id_types = Id_types.objects.get(id=id)
        id_types_serializer = Id_typesSerializer(id_types, data=id_types_data)

        if id_types_serializer.is_valid():
            id_types_serializer.save()
            return JsonResponse("Updated successfully!", safe=False)
        else:
            return JsonResponse("Failed to update.", safe=False)

    elif request.method == 'DELETE':
        id_types = Id_types.objects.get(id=id)
        id_types.delete()
        return JsonResponse("Deleted successfully!", safe=False)

#Item_categories
@csrf_exempt
def Item_categoriesApi(request, id=0):
    if request.method == 'GET':
        item_categories = Item_categories.objects.all()
        item_categories_serializer = Item_categoriesSerializer(item_categories, many=True)
        return JsonResponse(item_categories_serializer.data, safe=False)

    elif request.method == 'POST':
        item_categories_data = JSONParser().parse(request)
        item_categories_serializer = Item_categoriesSerializer(data=item_categories_data)

        if item_categories_serializer.is_valid():
            item_categories_serializer.save()
            return JsonResponse("Added successfully!", safe=False)
        else:
            return JsonResponse("Failed to add.", safe=False)

    elif request.method == 'PUT':
        item_categories_data = JSONParser().parse(request)
        item_categories = Item_categories.objects.get(id=id)
        item_categories_serializer = Item_categoriesSerializer(item_categories, data=item_categories_data)

        if item_categories_serializer.is_valid():
            item_categories_serializer.save()
            return JsonResponse("Updated successfully!", safe=False)
        else:
            return JsonResponse("Failed to update.", safe=False)

    elif request.method == 'DELETE':
        item_categories = Item_categories.objects.get(id=id)
        item_categories.delete()
        return JsonResponse("Deleted successfully!", safe=False)


# item_statuses
@csrf_exempt
def Item_statuses_api(request, id=0):
    if request.method == 'GET':
        item_statuses = Item_statuses.objects.all()
        item_statuses_serializer = Item_statusesSerializer(item_statuses, many=True)
        return JsonResponse(item_statuses_serializer.data, safe=False)

    elif request.method == 'POST':
        item_statuses_data = JSONParser().parse(request)
        item_statuses_serializer = Item_statusesSerializer(data=item_statuses_data)

        if item_statuses_serializer.is_valid():
            item_statuses_serializer.save()
            return JsonResponse("Added successfully!", safe=False)
        else:
            return JsonResponse("Failed to add.", safe=False)

    elif request.method == 'PUT':
        item_statuses_data = JSONParser().parse(request)
        item_statuses = Item_statuses.objects.get(id=id)
        item_statuses_serializer = Item_statusesSerializer(item_statuses, data=item_statuses_data)

        if item_statuses_serializer.is_valid():
            item_statuses_serializer.save()
            return JsonResponse("Updated successfully!", safe=False)
        else:
            return JsonResponse("Failed to update.", safe=False)
        
    elif request.method == 'DELETE':
        item_statuses = Item_statuses.objects.get(id=id)
        item_statuses.delete()
        return JsonResponse("Deleted successfully!", safe=False)

#Borrow_statuses
@csrf_exempt
def Borrow_statusesApi(request, id=0):
    if request.method == 'GET':
        borrow_statuses = Borrow_statuses.objects.all()
        borrow_statuses_serializer = Borrow_statusesSerializer(borrow_statuses, many=True)
        return JsonResponse(borrow_statuses_serializer.data, safe=False)

    elif request.method == 'POST':
        borrow_statuses_data = JSONParser().parse(request)
        borrow_statuses_serializer = Borrow_statusesSerializer(data=borrow_statuses_data)

        if borrow_statuses_serializer.is_valid():
            borrow_statuses_serializer.save()
            return JsonResponse("Added successfully!", safe=False)
        else:
            return JsonResponse("Failed to add.", safe=False)

    elif request.method == 'PUT':
        borrow_statuses_data = JSONParser().parse(request)
        borrow_statuses = Borrow_statuses.objects.get(id=id)
        borrow_statuses_serializer = Borrow_statusesSerializer(borrow_statuses, data=borrow_statuses_data)

        if borrow_statuses_serializer.is_valid():
            borrow_statuses_serializer.save()
            return JsonResponse("Updated successfully!", safe=False)
        else:
            return JsonResponse("Failed to update.", safe=False)

    elif request.method == 'DELETE':
        borrow_statuses = Borrow_statuses.objects.get(id=id)
        borrow_statuses.delete()
        return JsonResponse("Deleted successfully!", safe=False)
    
#Item
@csrf_exempt
def ItemApi(request, id=0):
    if request.method == 'GET':
        item = Item.objects.all()
        item_serializer = ItemSerializer(Item, many=True)
        return JsonResponse(item_serializer.data, safe=False)

    elif request.method == 'POST':
        item_data = JSONParser().parse(request)
        item_serializer = ItemSerializer(data=item_data)
        print(item_serializer)
        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse("Added successfully!", safe=False)
        else:
            return JsonResponse("Failed to add.", safe=False)

    elif request.method == 'PUT':
        item_data = JSONParser().parse(request)
        item = Item.objects.get(id=id)
        item_serializer = ItemSerializer(item, data=item_data)

        if item_serializer.is_valid():
            item_serializer.save()
            return JsonResponse("Updated successfully!", safe=False)
        else:
            return JsonResponse("Failed to update.", safe=False)

    elif request.method == 'DELETE':
        item = Item.objects.get(id=id)
        item.delete()
        return JsonResponse("Deleted successfully!", safe=False)

#Borrow_info
def borrow_info_api(request, id=0):
    if request.method == 'GET':
        if id:
            borrow_info = Borrow_info.objects.get(id=id)
            borrow_info_serializer = Borrow_infoSerializer(borrow_info)
            return JsonResponse(borrow_info_serializer.data)
        else:
            borrow_infos = Borrow_info.objects.all()
            borrow_info_serializer = Borrow_infoSerializer(borrow_infos, many=True)
            return JsonResponse(borrow_info_serializer.data, safe=False)

    elif request.method == 'POST':
        borrow_info_data = JSONParser().parse(request)
        borrow_info_serializer = Borrow_infoSerializer(data=borrow_info_data)
        if borrow_info_serializer.is_valid():
            borrow_info_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        borrow_info_data = JSONParser().parse(request)
        borrow_info = Borrow_info.objects.get(id=id)
        borrow_info_serializer = Borrow_infoSerializer(borrow_info, data=borrow_info_data)
        if borrow_info_serializer.is_valid():
            borrow_info_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        borrow_info = Borrow_info.objects.get(id=id)
        borrow_info.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)