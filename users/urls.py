from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [
    path('create_user/', views.create_user, name='create-user'),
    path('', views.list_users, name='list-users'),
    path('user_detail/<int:pk>', views.user_details, name='single-user'),

]
