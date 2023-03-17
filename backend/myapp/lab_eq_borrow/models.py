from django.db import models
from .storages import MediaStorage
# Create your models here.

class Borrow_status(models.Model):
    b_status_id = models.AutoField(primary_key=True)
    b_status_name = models.CharField(max_length=100)
    
    class Meta:
        db_table = "borrow_statuses"

    def __str__(self):
        return self.b_status_name
    
class User_privilege(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=100)

    class Meta:
        db_table = "user_privileges"
        
    def __str__(self):
        return self.p_name

class Major(models.Model):
    m_id = models.AutoField(primary_key=True)
    m_name = models.CharField(max_length=100)

    class Meta:
        db_table = "Majors"

    def __str__(self):
        return self.d_name

class Department(models.Model):
    d_id = models.AutoField(primary_key=True)
    d_name = models.CharField(max_length=100)

    class Meta:
        db_table = "departments"

    def __str__(self):
        return self.f_name

class Id_type(models.Model):
    t_id = models.AutoField(primary_key=True)
    t_name = models.CharField(max_length=100)

    class Meta:
        db_table = "id_types"

    def __str__(self):
        return self.t_name

class Item_category(models.Model):
    item_cate_id = models.AutoField(primary_key=True)
    item_cate_name =models.CharField(max_length=100)

    class Meta:
        db_table = "item_categories"

    def __str__(self):
        return self.item_cate_name
    
class Item_status(models.Model):
    item_status_id = models.AutoField(primary_key=True)
    item_status_name = models.CharField(max_length=100)

    class Meta:
        db_table = "item_statuses"

    def __str__(self):
        return self.item_status_name

class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    u_name = models.CharField(max_length=100, unique=True)
    u_password = models.CharField(max_length=100)
    u_email = models.EmailField(max_length=100,unique=True )
    u_tel = models.IntegerField()
    u_department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, related_name='users')
    u_major = models.ForeignKey(Major, on_delete=models.DO_NOTHING, related_name='users')
    u_privilege = models.ForeignKey(User_privilege, on_delete=models.DO_NOTHING, related_name='users')
    u_created_at = models.DateTimeField(auto_now_add=True)
    u_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"

    def __str__(self):
        return "%s %s %s" % (self.u_name,self.u_department,self.u_major)
    
class Item(models.Model):
    item_id = models.CharField(primary_key =True,max_length=50)
    item_id_type = models.ForeignKey(Id_type, on_delete = models.DO_NOTHING)
    item_name = models.CharField(max_length=100)
    item_category = models.ForeignKey(Item_category,on_delete = models.DO_NOTHING)
    item_description = models.TextField()
    item_department = models.ForeignKey(Department, on_delete = models.DO_NOTHING)
    item_major = models.ForeignKey(Major,on_delete = models.DO_NOTHING)
    item_status = models.ForeignKey(Item_status,on_delete = models.DO_NOTHING)
    item_borrow_status = models.ForeignKey(Borrow_status, on_delete = models.DO_NOTHING)
    item_note = models.TextField()
    item_img_url = models.FileField(storage=MediaStorage,upload_to = 'media/',blank=True, null=True) 
    item_created_at = models.DateTimeField(auto_now_add=True)
    item_updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "items"
    def __str__(self):
        return self.item_name
    
    def s3_url(self):
        return self.item_img_url.url


class Borrow_info(models.Model):
    b_id = models.AutoField(primary_key =True)
    b_item = models.ForeignKey(Item, on_delete=models.DO_NOTHING,max_length=50)
    b_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    b_location = models.TextField()
    b_note = models.TextField()
    b_borrow_time = models.DateTimeField()
    b_return_time = models.DateTimeField()
    b_created_at = models.DateTimeField(auto_now_add=True)
    b_updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "borrow_info"
    def __str__(self):
        return self.b_user

