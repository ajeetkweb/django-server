from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [
    path('create_user/', views.create_user),
    path('', views.list_users),
    path('user_detail/<int:pk>', views.user_details),

]
