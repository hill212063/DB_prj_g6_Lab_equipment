from django.urls import re_path,path
from Main import views
from .views import *

urlpatterns = [
    re_path(r'^faculty$',views.facultyApi),
    re_path(r'^faculty/([0-9]+)$',views.facultyApi),

    re_path(r'^department$',views.departmentApi),
    re_path(r'^department/([0-9]+)$',views.departmentApi),

    re_path(r'^user_privilege$',views.user_privileges_api),
    re_path(r'^user_privilege/([0-9]+)$',views.user_privileges_api),

    re_path(r'^user$',views.user_api),
    re_path(r'^user/([0-9]+)$',views.user_api),

    re_path(r'^Id_types$',views.Id_typesApi),
    re_path(r'^Id_types/([0-9]+)$',views.Id_typesApi),

    re_path(r'^Item_categories$',views.Item_categoriesApi),
    re_path(r'^Item_categories/([0-9]+)$',views.Item_categoriesApi),

    re_path(r'^Item_statuses$',views.Item_statuses_api),
    re_path(r'^Item_statuses/([0-9]+)$',views.Item_statuses_api),

    re_path(r'^Borrow_statuses$',views.Borrow_statusesApi),
    re_path(r'^Borrow_statuses/([0-9]+)$',views.Borrow_statusesApi),

    re_path(r'^Item$',views.ItemApi),
    re_path(r'^Item/([0-9]+)$',views.ItemApi),

    re_path(r'^Borrow_info$',views.borrow_info_api),
    re_path(r'^Borrow_info/([0-9]+)$',views.borrow_info_api),

    path('api/login/', LoginAPIView.as_view()),
    path('api/register', RegisterAPIView.as_view()),
    path('api/user', UserAPIView.as_view()),
    path('api/refresh', RefreshAPIView.as_view()),
    path('api/logout', LogoutAPIView.as_view()),    

]
