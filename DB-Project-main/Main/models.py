from django.db import models

# Create your models here.

class Faculty(models.Model):
    name = models.CharField(max_length=100)

class Department(models.Model):
    name = models.CharField(max_length=100)

class User_privileges(models.Model):
    name = models.CharField(max_length=100)

class Id_types(models.Model):
    name = models.CharField(max_length=100)

class Item_categories(models.Model):
    name = models.CharField(max_length=100)

class Item_statuses(models.Model):
    name = models.CharField(max_length=100)

class Borrow_statuses(models.Model):
    name = models.CharField(max_length=100)

class User(models.Model):
    u_name = models.CharField(max_length=200)
    u_password = models.CharField(max_length=200)
    u_email = models.CharField(max_length=200)
    u_tel = models.IntegerField()
    u_faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='users_faculty')
    u_department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='users_department')
    u_privilege = models.ForeignKey(User_privileges, on_delete=models.CASCADE, related_name='users_privilege')
    u_create_at = models.DateTimeField(auto_now_add=True)
    u_update_at = models.DateTimeField(auto_now=True)

class Item (models.Model):
    item_id = models.CharField(max_length=200)
    item_id_type = models.ForeignKey(Id_types, on_delete=models.CASCADE, related_name='item_id_type')
    item_name = models.CharField(max_length=200)
    item_category = models.ForeignKey(Item_categories, on_delete=models.CASCADE, related_name='item_item_categories')
    item_description = models.CharField(max_length=200)
    item_faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='item_faculty')
    item_department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='item_department')
    item_status = models.ForeignKey(Item_statuses, on_delete=models.CASCADE, related_name='item_status')
    item_borrow_status = models.ForeignKey(Borrow_statuses, on_delete=models.CASCADE, related_name='item_borrow_status')
    item_note = models.CharField(max_length=200)
    item_img_url = models.CharField(max_length=200)
    item_create_at = models.DateTimeField(auto_now_add=True)
    item_update_at = models.DateTimeField(auto_now=True)

class Borrow_info (models.Model):
    b_item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='borrow_info_item')
    b_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrow_info_user')
    b_location = models.CharField(max_length=200)
    b_note =  models.CharField(max_length=200)
    b_borrow_time = models.DateTimeField(auto_now=True)
    b_return_time = models.DateTimeField(auto_now=True)
    b_create_at = models.DateTimeField(auto_now_add=True)
    b_update_at = models.DateTimeField(auto_now=True)