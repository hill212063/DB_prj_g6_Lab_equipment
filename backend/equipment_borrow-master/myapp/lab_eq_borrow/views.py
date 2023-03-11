from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect,JsonResponse
from django.template import loader
from .models import *
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .serializers import *

from .authentication import create_access_token, create_refresh_token , decode_access_token , decode_refresh_token
from .permissions import *
from .backends import *

# Create your views here.
def index(request):
    objs = Item.objects.all().values()
    json_data = []
    for obj in objs:
        json_data.append(obj)

    return JsonResponse(json_data, safe=False, json_dumps_params={'ensure_ascii': False})

# Set the refresh token as a cookie in the response
def set_refresh_token(response, refresh_token):
    response.set_cookie('refresh_token', refresh_token, httponly=True, max_age=604800)  # 7 days in seconds

# Get the refresh token from the request cookies
def get_refresh_token(request):
    return request.COOKIES.get('refresh_token')


@api_view(['GET'])
def all_faculties(request):
    allfaculties = Facultie.objects.all()
    serializer = FacultiesSerializer(allfaculties,many = True)
    return Response(serializer.data,status = status.HTTP_200_OK)

@api_view(['GET'])
def all_items(request):
    allitems = Item.objects.all()
    serializer = ItemsSerializer(allitems,many = True)
    return Response(serializer.data,status = status.HTTP_200_OK)



from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
#@permission_classes([IsAuthenticated, CanViewItems])
def items(request):
    # TODO: Implement logic to fetch and return equipments for student users
    allitems = Item.objects.all()
    serializer = ItemsSerializer(allitems,many = True)
    return Response(serializer.data,status = status.HTTP_200_OK)

@api_view(['GET'])
#@permission_classes([IsAuthenticated, CanViewItemDetails])
def item_details(request, item_id):
    try:
        item = Item.objects.get(item_id=item_id)
        data = {
            'item_id': item.item_id,
            'item_name': item.item_name,
            'item_category': item.item_category,
            'item_description': item.item_description,
            'item_faculty': item.item_faculty,
            'item_department': item.item_department,
            'item_status': item.item_status,
            'item_borrow_status': item.item_borrow_status,
            'item_note': item.item_note,
            'item_img_url': item.item_img_id.url,
            'item_created_at': item.item_created_at,
            'item_updated_at': item.item_updated_at,
        }
        return JsonResponse(data)
    except Item.DoesNotExist:
        return JsonResponse({'error': 'Item does not exist'})

@api_view(['GET'])
#@permission_classes([IsAuthenticated, CanViewItemDetails])
def contact(request, equipment_id):
    # TODO: Implement logic to fetch and return contact info for equipment_id for student users
    response_data = {'message': f'Contact info for equipment {equipment_id} for student users'}
    return JsonResponse(response_data)

@api_view(['GET'])
#@permission_classes([IsAuthenticated, IsStudent])
def borrowed_equipment(request):
    # TODO: Implement logic to fetch and return borrowed equipment for student users
    response_data = {'message': 'List of borrowed equipments for student users'}
    return JsonResponse(response_data)




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
      
        access_token = create_access_token(user.u_id,str(user.u_privilege))
        refresh_token = create_refresh_token(user.u_id,str(user.u_privilege))

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