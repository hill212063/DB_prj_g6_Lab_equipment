from django.urls import path
from .views import *
urlpatterns = [
    path('', index),
    path('api/all-faculties/', all_faculties),
    path('api/all-items/', all_items),

    path('api/login/', LoginAPIView.as_view()),
    path('api/register', RegisterAPIView.as_view()),
    path('api/user', UserAPIView.as_view()),
    path('api/refresh', RefreshAPIView.as_view()),
    path('api/logout', LogoutAPIView.as_view()),

    path('api/items/', items),
    path('api/items/<int:item_id>/', item_details),
    path('api/contact/<int:equipment_id>/', contact),
    path('api/borrowed/', borrowed_equipment),


]

