from rest_framework import serializers
from Main.models import Faculty, Department, User_privileges, Id_types, Item_categories, Item_statuses, Borrow_statuses, User, Item, Borrow_info

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['id', 'name']

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']

class User_privilegesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_privileges
        fields = ['id', 'name']

class Id_typesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Id_types
        fields = ['id', 'name']

class Item_categoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_categories
        fields = ['id', 'name']

class Item_statusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_statuses
        fields = ['id', 'name']

class Borrow_statusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow_statuses
        fields = ['id', 'name']

class UserSerializer(serializers.ModelSerializer):
    u_faculty = serializers.PrimaryKeyRelatedField(queryset=Faculty.objects.all())
    u_department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    u_privilege = serializers.PrimaryKeyRelatedField(queryset=User_privileges.objects.all())

    class Meta:
        model = User
        fields = ['id', 'u_name', 'u_password', 'u_email', 'u_tel', 'u_faculty', 'u_department', 'u_privilege', 'u_create_at', 'u_update_at']

class ItemSerializer(serializers.ModelSerializer):
    item_id_type = serializers.PrimaryKeyRelatedField(queryset=Id_types.objects.all())
    item_category = serializers.PrimaryKeyRelatedField(queryset=Item_categories.objects.all())
    item_faculty = serializers.PrimaryKeyRelatedField(queryset=Faculty.objects.all())
    item_department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    item_status = serializers.PrimaryKeyRelatedField(queryset=Item_statuses.objects.all())
    item_borrow_status = serializers.PrimaryKeyRelatedField(queryset=Borrow_statuses.objects.all())

    class Meta:
        model = Item
        fields = ['id', 'item_id', 'item_id_type', 'item_name', 'item_category', 'item_description', 'item_faculty', 'item_department', 'item_status', 'item_borrow_status', 'item_note', 'item_img_url', 'item_create_at', 'item_update_at']

class Borrow_infoSerializer(serializers.ModelSerializer):
    b_item = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all())
    b_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Borrow_info
        fields = ['id', 'b_item', 'b_user', 'b_location', 'b_note', 'b_borrow_time', 'b_return_time', 'b_create_at', 'b_update_at']
