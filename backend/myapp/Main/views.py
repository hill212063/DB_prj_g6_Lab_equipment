from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect,JsonResponse
from django.template import loader
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .authentication import create_access_token, create_refresh_token , decode_access_token , decode_refresh_token
#from .permissions import *
from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import APIException , AuthenticationFailed

import os
import uuid
from .storages import MediaStorage
from datetime import datetime  
from .models import *
from .serializers import *

@api_view(['GET'])
def update_expire():
    try:
        expire_status = Borrow_status.objects.filter(b_status_name="expire") 
        expired_items = Borrow_info.objects.filter(b_return_time__lte=datetime.now())
        for i in expired_items:
            Item.objects.filter(item_id = i.b_item).update(item_status = expire_status.b_status_id)
        return Response({'message':'Expire Item updated'},status = status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def all_faculties(request):
    try:
        allfaculties = Faculty.objects.all()
        serializer = FacultySerializer(allfaculties,many = True)
        return Response(serializer.data,status = status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def all_departments(request):
    try:
        alldepartments = Department.objects.all()
        serializer = DepartmentSerializer(alldepartments,many = True)
        return Response(serializer.data,status = status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def all_items(request):
    try:
        allitems = Item.objects.all()
        serializer = ItemSerializer(allitems,many = True)
        return Response(serializer.data,status = status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
#@permission_classes([IsAuthenticated, CanViewItems])
def items(request):
    # get only item that borrowed
    try:
        available_status = Borrow_status.objects.filter(b_status_name="available") 
        allitems = Item.objects.filter(item_status =  available_status.b_status_id )
        serializer = ItemSerializer(allitems,many = True)
        return Response(serializer.data,status = status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
#@permission_classes([IsAuthenticated, CanViewItemDetails])
def item_details(request, item_id):
    try:
        item = Item.objects.get(item_id=item_id)
        data = {
            'item_id': item.item_id,
            'item_id_type':item.item_id_type,
            'item_name': item.item_name,
            'item_category': item.item_category,
            'item_description': item.item_description,
            'item_faculty': item.item_faculty,
            'item_department': item.item_department,
            'item_status': item.item_status,
            'item_borrow_status': item.item_borrow_status,
            'item_note': item.item_note,
            'item_img_url': item.item_img_url,
            'item_created_at': item.item_created_at,
            'item_updated_at': item.item_updated_at,
        }
        return JsonResponse(data)
    except Item.DoesNotExist:
        return JsonResponse({'error': 'Item does not exist'})

@api_view(['GET'])
#@permission_classes([IsAuthenticated, CanViewItemDetails])
def contact(request):
    # TODO: Implement logic to fetch and return contact info for equipment_id for student users
    response_data = {'message': f'Contact Admin'}
    return JsonResponse(response_data)

@api_view(['GET'])
#@permission_classes([IsAuthenticated, IsStudent])
def borrowed_item(request):
    try:
        update_expire()
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    try:
        borrowings = Borrow_info.objects.filter(b_user=request.user)
        borrowed_items = []
        for borrowing in borrowings:
            item = borrowing.b_item
            item_data = {
                'item_id': item.item_id,
                'item_id_type': item.item_id_type,
                'item_name': item.item_name,
                'item_category': item.item_category,
                'item_description': item.item_description,
                'item_faculty': item.item_faculty.faculty_name, # Accessing faculty name from Faculty model
                'item_department': item.item_department.department_name, # Accessing department name from Department model
                'item_status': item.item_borrow_status.b_status_name # Accessing borrow status name from Borrow_statuse model
            }
            borrowed_items.append(item_data,status = status.HTTP_200_OK)
        return Response(borrowed_items)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET'])
def user_management(request):
    try:
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

from django.core.exceptions import ObjectDoesNotExist

@api_view(['POST'])
def add_user(request):
    '''
    Expected request body:
    {
        "u_name": "User Name",
        "u_email": "user@email.com",
        "u_password": "password",
        "u_tel": "1234567890",
        "u_faculty": 1,  // Faculty id
        "u_department": 1,  // Department id
        "u_privilege": 1  // User privileges id
    }
    '''

    try:
        # Retrieve data from request body
        u_name = request.data.get('u_name')
        u_email = request.data.get('u_email')
        u_password = request.data.get('u_password')
        u_tel = request.data.get('u_tel')
        u_faculty_id = request.data.get('u_faculty')
        u_department_id = request.data.get('u_department')
        u_privilege_id = request.data.get('u_privilege')

        # Check if faculty exists
        try:
            u_faculty = Faculty.objects.get(f_id=u_faculty_id)
        except ObjectDoesNotExist:
            return Response({'message': 'Faculty not found'}, status=status.HTTP_404_NOT_FOUND)

        # Check if department exists
        try:
            u_department = Department.objects.get(d_id=u_department_id)
        except ObjectDoesNotExist:
            return Response({'message': 'Department not found'}, status=status.HTTP_404_NOT_FOUND)

        # Check if user privilege exists
        try:
            u_privilege = User_privilege.objects.get(p_id=u_privilege_id)
        except ObjectDoesNotExist:
            return Response({'message': 'User privilege not found'}, status=status.HTTP_404_NOT_FOUND)

        # Create new user instance
        inserted_data = User(
            u_name=u_name,
            u_email=u_email,
            u_password=u_password,
            u_tel=u_tel,
            u_faculty=u_faculty,
            u_department=u_department,
            u_privilege=u_privilege
        )
        inserted_data.save()

        return Response({'message': 'Added'}, status=status.HTTP_200_OK)
        
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def edit_user(request,user_id):
    '''
    Expected request body:
    {
        u_name
        u_email
        u_password
        u_tel
        u_faculty
        u_department
        u_privilege
    }
    '''
    try:
        try:
            exist_data = User.objects.get(u_id = user_id)
        except ObjectDoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        exist_data.u_name = request.data.get('u_name')
        exist_data.u_email = request.data.get('u_email')
        exist_data.u_password = request.data.get('u_password')
        exist_data.u_tel = request.data.get('u_tel')
        try:
            exist_data.u_faculty = Faculty.objects.get(f_id=request.data.get('u_faculty'))
        except ObjectDoesNotExist:
            return Response({'message': 'Faculty not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
            exist_data.u_department = Department.objects.get(d_id=request.data.get('u_department'))
        except ObjectDoesNotExist:
            return Response({'message': 'Department not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
            exist_data.u_privilege = User_privilege.objects.get(p_id =request.data.get('u_privilege'))
        except ObjectDoesNotExist:
            return Response({'message': 'User privilege not found'}, status=status.HTTP_404_NOT_FOUND)
        
        exist_data.save()
        return Response({'message':'Edited'},status = status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def delete_user(request,user_id):
    try:
        user = User.objects.get(u_id = user_id)
        user.delete()
        return Response({'message':'Deleted'},status = status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





@api_view(['GET'])
def borrowing_info(request):
    try:
        b_infos = Borrow_info.objects.all()
        serializer = BorrowInfoSerializer( b_infos,many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['POST'])
def add_borrowing_info(request):
    ''' หน้าตาของ request
    b_item
    b_user
    b_borrow_time
    b_return_time
    b_location
    b_note
    '''
    try:
        try:
            b_item=Item.objects.get(item_id= request.data.get('b_item'))
        except ObjectDoesNotExist:
            return Response({'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
            b_user=User.objects.get(item_id= request.data.get('b_item'))
        except ObjectDoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        b_borrow_time=request.data.get('b_borrow_time')
        b_return_time=request.data.get('b_return_time')
        b_location=request.data.get('b_location')
        b_note = request.data.get('b_note')
        inserted_data = User.objects.create(
            b_item= b_item,
            b_user=b_user,
            b_borrow_time=b_borrow_time,
            b_return_time=b_return_time,
            b_location= b_location,
            b_note =  b_note
        )
        inserted_data.save()
        return Response({'message':'Added'},status = status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['POST'])
def edit_borrowing_info(request,info_id):
    ''' หน้าตาของ request
    b_item
    b_user
    b_borrow_time
    b_return_time
    b_location
    b_note
    '''
    try:
        try:
            exist_data = Borrow_info.objects.get(b_id = info_id)
        except ObjectDoesNotExist:
            return Response({'message': 'Borrow info not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
            exist_data.b_item = Item.objects.get(item_id=request.data.get('b_item'))
        except ObjectDoesNotExist:
            return Response({'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
            exist_data.b_user = User.objects.get(u_id=request.data.get('b_user'))
        except ObjectDoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        exist_data.b_borrow_time = request.data.get('b_borrow_time')
        exist_data.b_return_time = request.data.get('b_return_time')
        exist_data.b_location = request.data.get('b_location')
        exist_data.b_note = request.data.get('b_note')
        exist_data.save()
        return Response({'message':'Edited'},status = status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['DELETE'])
def delete_borrowing_info(request,info_id):
    try:
        b_info = Borrow_info.objects.get(b_id = info_id)
        b_info.delete()
        return Response({'message':'Deleted'},status = status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(['GET'])
def item_info(request):
    try:
        item_infos = Item.objects.all()
        serializer = ItemSerializer( item_infos,many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def add_item_info(request):
    '''request:
    item_id
    item_id_type
    item_name
    item_category
    item_faculty
    item_department
    item_status
    item_borrow_status
    item_description
    item_note
    file as image file
    '''
    try:
        item_id=request.data.get('item_id')
        try:
            item_id_type = Id_type.objects.get(t_id=request.data.get('item_id_type'))
        except ObjectDoesNotExist:
            return Response({'message': 'Id type not found'}, status=status.HTTP_404_NOT_FOUND)
        
        item_name=request.data.get('item_name')

        try:
            item_category=Item_category.objects.get(item_cate_id=request.data.get('item_category'))
        except ObjectDoesNotExist:
            return Response({'message': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            item_faculty=Faculty.objects.get(f_id= request.data.get('item_faculty'))
        except ObjectDoesNotExist:
            return Response({'message': 'Faculty not found'}, status=status.HTTP_404_NOT_FOUND)
        
        try:
            item_department=Department.objects.get(d_id=request.data.get('item_department'))
        except ObjectDoesNotExist:
            return Response({'message': 'Department not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
            item_status=Item_status.objects.get(item_status_id= request.data.get('item_status'))
        except ObjectDoesNotExist:
            return Response({'message': 'Item status not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
            item_borrow_status=Borrow_status.objects.get(b_status_id= request.data.get('item_borrow_status'))
        except ObjectDoesNotExist:
            return Response({'message': 'Borrow status not found'}, status=status.HTTP_404_NOT_FOUND)
        item_description=request.data.get('item_description')
        item_note=request.data.get('item_note')


        #FOR UPLOAD FILE
        file_path_within_bucket=""
        media_storage = MediaStorage()
        if(request.FILES.get('file', False)):
            file_obj = request.FILES.get('file', '')

            # do your validation here e.g. file size/type check

            # organize a path for the file in bucket
            file_directory_within_bucket = 'media/'
            file_type = '.'+file_obj.name.split('.')[1]
            # synthesize a full file path; note that we included the filename
            file_path_within_bucket = os.path.join(
                file_directory_within_bucket,
                str(uuid.uuid4())+file_type
            )
            if not media_storage.exists(file_path_within_bucket): # avoid overwriting existing file
                media_storage.save(file_path_within_bucket, file_obj)
                file_url = media_storage.url(file_path_within_bucket)
            else:
                return Response({
                    'message': 'Error: file {filename} already exists at {file_directory} in bucket {bucket_name}'.format(
                        filename=file_obj.name,
                        file_directory=file_directory_within_bucket,
                        bucket_name=media_storage.bucket_name
                    ),
                }, status=400)

        inserted_data = Item(
            item_id=item_id,
            item_id_type= item_id_type,
            item_name=item_name,
            item_category=item_category,
            item_faculty=item_faculty,
            item_department=item_department,
            item_status=item_status,
            item_borrow_status=item_borrow_status,
            item_description=item_description,
            item_note=item_note,
            item_img_url=file_path_within_bucket
        )
        inserted_data.save()
        return Response({'message':'Added'},status = status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def edit_item_info(request, item_id):
    '''request:
    item_id
    item_id_type
    item_name
    item_category
    item_faculty
    item_department
    item_status
    item_borrow_status
    item_description
    item_note
    file as image file
    '''
    try:
        try:
            exist_data = Item.objects.get(item_id=item_id)
        except ObjectDoesNotExist:
            return Response({'message': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
            exist_data.item_id_type =Id_type.objects.get(t_id= request.data.get('item_id_type'))
        except ObjectDoesNotExist:
            return Response({'message': 'Id type not found'}, status=status.HTTP_404_NOT_FOUND)
        
        exist_data.item_name = request.data.get('item_name')

        try:
            exist_data.item_category =Item_category.objects.get(item_cate_id= request.data.get('item_category'))
        except ObjectDoesNotExist:
            return Response({'message': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
            exist_data.item_faculty =Faculty.objects.get(f_id=  request.data.get('item_faculty'))
        except ObjectDoesNotExist:
            return Response({'message': 'Faculty not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
            exist_data.item_department = Department.objects.get(d_id=request.data.get('item_department'))
        except ObjectDoesNotExist:
            return Response({'message': 'Department not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
            exist_data.item_status =Item_status.objects.get(item_status_id= request.data.get('item_status'))
        except ObjectDoesNotExist:
            return Response({'message': 'Item status not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
            exist_data.item_borrow_status = Borrow_status.objects.get(b_status_id= request.data.get('item_borrow_status'))
        except ObjectDoesNotExist:
            return Response({'message': 'Borrow status not found'}, status=status.HTTP_404_NOT_FOUND)
        exist_data.item_description = request.data.get('item_description')
        exist_data.item_note = request.data.get('item_note')
        #FOR UPLOAD FILE
        file_path_within_bucket=""
        media_storage = MediaStorage()
        if(request.FILES.get('file', False)):
            file_obj = request.FILES.get('file', '')

            # do your validation here e.g. file size/type check

            # organize a path for the file in bucket
            file_directory_within_bucket = 'media/'
            file_type = '.'+file_obj.name.split('.')[1]
            # synthesize a full file path; note that we included the filename
            file_path_within_bucket = os.path.join(
                file_directory_within_bucket,
                str(uuid.uuid4())+file_type
            )
            exist_data.item_img_url.delete() 
            if not media_storage.exists(file_path_within_bucket): # avoid overwriting existing file
                media_storage.save(file_path_within_bucket, file_obj)
                file_url = media_storage.url(file_path_within_bucket)
            else:
                return Response({
                    'message': 'Error: file {filename} already exists at {file_directory} in bucket {bucket_name}'.format(
                        filename=file_obj.name,
                        file_directory=file_directory_within_bucket,
                        bucket_name=media_storage.bucket_name
                    ),
                }, status=400)
            exist_data.item_img_url = file_path_within_bucket

        exist_data.save()
        return Response({'message':'Edited'},status = status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def delete_item_info(request,item_id):
    try:
        item_info = Item.objects.get(item_id = item_id)
        item_info.item_img_url.delete()
        item_info.delete()
        return Response({'message':'Deleted'},status = status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



#AUTH SYSTEM
# Set the refresh token as a cookie in the response
def set_refresh_token(response, refresh_token):
    response.set_cookie('refresh_token', refresh_token, httponly=True, max_age=604800)  # 7 days in seconds

# Get the refresh token from the request cookies
def get_refresh_token(request):
    return request.COOKIES.get('refresh_token')

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