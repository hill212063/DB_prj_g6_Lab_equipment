from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from Main.models import Faculty, Department, User_privileges, User
from Main.serializers import FacultySerializer, DepartmentSerializer, User_privilegesSerializer, UserSerializer

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
        faculty = Faculty.objects.get(id=faculty_data['id'])
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
        department = Department.objects.get(id=department_data['id'])
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
        user_privilege = User_privileges.objects.get(id=user_privilege_data['id'])
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
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)

    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = User.objects.get(id=user_data['id'])
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method == 'DELETE':
        user = User.objects.get(id=id)
        user.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)