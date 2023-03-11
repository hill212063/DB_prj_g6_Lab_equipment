from django import forms
from .models import Facultie, Department, User_privilege, Item_categorie, Id_type, Item_statuse, Borrow_statuse

class UserForm(forms.Form):
    u_name = forms.CharField(max_length=100)
    u_email = forms.EmailField(max_length=100)
    u_password = forms.CharField(max_length=100)
    u_tel = forms.IntegerField()
    u_faculty = forms.ModelChoiceField(queryset=Facultie.objects.all())
    u_department = forms.ModelChoiceField(queryset=Department.objects.all())
    u_privilege = forms.ModelChoiceField(queryset=User_privilege.objects.all())

class BorrowInfoForm(forms.Form):
    item_name = forms.CharField(max_length=100)
    user = forms.CharField(max_length=100)
    borrow_time = forms.DateTimeField()
    return_time = forms.DateTimeField()
    location = forms.CharField(widget=forms.Textarea)
    note = forms.CharField(widget=forms.Textarea)

class ItemForm(forms.Form):
    item_id = forms.CharField(max_length=100)
    item_name = forms.CharField(max_length=100)
    item_id_type = forms.ModelChoiceField(queryset=Id_type.objects.all())
    item_category = forms.ModelChoiceField(queryset=Item_categorie.objects.all())
    item_faculty = forms.ModelChoiceField(queryset=Facultie.objects.all())
    item_department = forms.ModelChoiceField(queryset=Department.objects.all())
    item_status = forms.ModelChoiceField(queryset=Item_statuse.objects.all())
    item_borrow_status = forms.ModelChoiceField(queryset=Borrow_statuse.objects.all())
    item_description = forms.CharField(widget=forms.Textarea)
    item_note = forms.CharField(widget=forms.Textarea)