from django.db import models

# Create your models here.

class Borrow_statuse(models.Model):
    b_status_id = models.AutoField(primary_key=True)
    b_status_name = models.CharField(max_length=100)

    def __str__(self):
        return self.b_status_name
    
class User_privilege(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_name = models.CharField(max_length=100)
    def __str__(self):
        return self.p_name

class Department(models.Model):
    d_id = models.AutoField(primary_key=True)
    d_name = models.CharField(max_length=100)
    def __str__(self):
        return self.d_name

class Facultie(models.Model):
    f_id = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=100)
    def __str__(self):
        return self.f_name

class Id_type(models.Model):
    t_id = models.AutoField(primary_key=True)
    t_name = models.CharField(max_length=100)
    def __str__(self):
        return self.t_name

class Item_categorie(models.Model):
    item_cate_id = models.AutoField(primary_key=True)
    item_cate_name =models.CharField(max_length=100)
    def __str__(self):
        return self.item_cate_name
    
class Item_statuse(models.Model):
    item_status_id = models.AutoField(primary_key=True)
    item_status_name = models.CharField(max_length=100)
    def __str__(self):
        return self.item_status_name

class User(models.Model):
    u_id = models.AutoField(primary_key=True)
    u_name = models.CharField(max_length=100, unique=True)
    u_password = models.CharField(max_length=100)
    u_email = models.EmailField(max_length=100,unique=True )
    u_tel = models.IntegerField()
    u_faculty = models.ForeignKey(Facultie, on_delete=models.DO_NOTHING, related_name='users')
    u_department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, related_name='users')
    u_privilege = models.ForeignKey(User_privilege, on_delete=models.DO_NOTHING, related_name='users')
    u_created_at = models.DateTimeField(auto_now_add=True)
    u_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s %s" % (self.u_name,self.u_faculty,self.u_department)
    
class Item(models.Model):
    item_id = models.AutoField(primary_key =True)
    item_id_type = models.ForeignKey(Id_type, on_delete = models.DO_NOTHING)
    item_name = models.CharField(max_length=100)
    item_category = models.ForeignKey(Item_categorie,on_delete = models.DO_NOTHING)
    item_description = models.TextField()
    item_faculty = models.ForeignKey(Facultie, on_delete = models.DO_NOTHING)
    item_department = models.ForeignKey(Department,on_delete = models.DO_NOTHING)
    item_status = models.ForeignKey(Item_statuse,on_delete = models.DO_NOTHING)
    item_borrow_status = models.ForeignKey(Borrow_statuse, on_delete = models.DO_NOTHING)
    item_note = models.TextField()
    item_img_id = models.ImageField()  # wait for insert params
    item_created_at = models.DateTimeField(auto_now_add=True)
    item_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item_name



class Borrow_info(models.Model):
    b_id = models.AutoField(primary_key =True)
    b_item = models.ForeignKey(Item, on_delete=models.CASCADE)
    b_user = models.ForeignKey(User, on_delete=models.CASCADE)
    b_location = models.TextField()
    #b_status = models.ForeignKey(Borrow_statuses, on_delete = models.CASCADE)
    b_note = models.TextField()
    b_borrow_time = models.DateTimeField()
    b_return_time = models.DateTimeField()
    b_created_at = models.DateTimeField(auto_now_add=True)
    b_updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.b_user

