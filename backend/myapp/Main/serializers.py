from rest_framework import serializers
from .models import Faculty, Department, User_privilege, Id_type, Item_category, Item_status, Borrow_status, User, Item, Borrow_info

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['f_id', 'f_name']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['d_id', 'd_name']

class User_privilegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_privilege
        fields = ['p_id', 'p_name']

class Id_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Id_type
        fields = ['t_id', 't_name']

class Item_categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_category
        fields = ['item_cate_id', 'item_cate_name']

class Item_statusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_status
        fields = ['item_status_id', 'item_status_name']

class Borrow_statusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow_status
        fields = ['b_status_id', 'b_status_name']

class UserSerializer(serializers.ModelSerializer):
    u_faculty = serializers.PrimaryKeyRelatedField(queryset=Faculty.objects.all())
    u_department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    u_privilege = serializers.PrimaryKeyRelatedField(queryset=User_privilege.objects.all())

    class Meta:
        model = User
        fields = ['u_id', 'u_name', 'u_password', 'u_email', 'u_tel', 'u_faculty', 'u_department', 'u_privilege', 'u_create_at', 'u_update_at']

class ItemSerializer(serializers.ModelSerializer):
    item_id_type = serializers.PrimaryKeyRelatedField(queryset=Id_type.objects.all())
    item_category = serializers.PrimaryKeyRelatedField(queryset=Item_category.objects.all())
    item_faculty = serializers.PrimaryKeyRelatedField(queryset=Faculty.objects.all())
    item_department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    item_status = serializers.PrimaryKeyRelatedField(queryset=Item_status.objects.all())
    item_borrow_status = serializers.PrimaryKeyRelatedField(queryset=Borrow_status.objects.all())

    class Meta:
        model = Item
        fields = ['item_id', 'item_id', 'item_id_type', 'item_name', 'item_category', 'item_description', 'item_faculty', 'item_department', 'item_status', 'item_borrow_status', 'item_note', 'item_img_url', 'item_create_at', 'item_update_at']

class Borrow_infoSerializer(serializers.ModelSerializer):
    b_item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())
    b_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Borrow_info
        fields = ['b_id', 'b_item', 'b_user', 'b_location', 'b_note', 'b_borrow_time', 'b_return_time', 'b_create_at', 'b_update_at']
