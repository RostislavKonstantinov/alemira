from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings

app_name = 'app_assignments'
urlpatterns = [
    path('assignment_list/', views.assignment_list, name='assignment_list'),
    path('assignment_details/<pk>/', views.assignment_details, name='assignment_details'),
    path('hint_list/', views.hint_list, name='hint_list'),
    path('hint_details/<pk>/', views.hint_details, name='hint_details'),
]





