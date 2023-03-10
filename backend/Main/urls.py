from django.urls import re_path
from Main import views

urlpatterns = [
    re_path(r'^faculty$',views.facultyApi),
    re_path(r'^faculty/([0-9]+)$',views.facultyApi),

    re_path(r'^department$',views.departmentApi),
    re_path(r'^department/([0-9]+)$',views.departmentApi),

    re_path(r'^user_privilege$',views.user_privileges_api),
    re_path(r'^user_privilege/([0-9]+)$',views.user_privileges_api),

    re_path(r'^user$',views.user_api),
    re_path(r'^user/([0-9]+)$',views.user_api)

]
