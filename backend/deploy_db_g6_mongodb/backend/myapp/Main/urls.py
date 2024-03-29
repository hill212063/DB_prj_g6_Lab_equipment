from django.urls import path
from .views import *
urlpatterns = [
    # path('', index),


    path('api/update-expire/',update_expire),

    path('api/all-departments/', all_departments),
    path('api/all-majors/', all_majors),
    path('api/all-items/', all_items),
    path('api/all-roles/',all_roles),
    path('api/all-idtypes/',all_idtypes),
    path('api/all-categories/',all_categories),
    path('api/all-item_statuses',all_item_statuses),




    path('api/login/', LoginAPIView.as_view()),
    path('api/register', RegisterAPIView.as_view()),
    # path('api/user', UserAPIView.as_view()),
    # path('api/refresh', RefreshAPIView.as_view()),
    path('api/logout', LogoutAPIView.as_view()),

    path('api/items/', items),
    path('api/items/<int:item_id>/', item_details),
    path('api/contact/', contact),
    path('api/borrowed/<int:user_id>/', borrowed),

    #path('api/dashboard/', dashboard),
    path('api/dashboard/user-management/', user_management),
    path('api/dashboard/user-management/add/', add_user),
    path('api/dashboard/user-management/edit/<int:user_id>/', edit_user),
    path('api/dashboard/user-management/delete/<int:user_id>/',delete_user),
    path('api/dashboard/user-management/<int:user_id>/', user_by_id),

    path('api/dashboard/borrowing-info/', borrowing_info),
    path('api/dashboard/borrowing-info/add/', add_borrowing_info),
    path('api/dashboard/borrowing-info/edit/<int:info_id>/', edit_borrowing_info),
    path('api/dashboard/borrowing-info/delete/<int:info_id>/', delete_borrowing_info),
    path('api/dashboard/borrowing-info/<int:info_id>/', borrowing_by_id),

    path('api/dashboard/item-info/', item_info),
    path('api/dashboard/item-info/add/', add_item_info),
    path('api/dashboard/item-info/edit/<str:item_id>/', edit_item_info),
    path('api/dashboard/item-info/delete/<str:item_id>/', delete_item_info),
    path('api/dashboard/item-info/<str:item_id>/', item_by_id),

]

