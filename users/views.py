from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Create your views here.

# Create your views here.

# function-based views


#create new user
@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)


# get list of users
@api_view(['GET'])
def list_users(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many = True)
    return Response(serializer.data)


# get, update and delete single user
@api_view(['GET', 'PUT', 'DELETE'])

def user_details(request, pk):

    if request.method == 'GET':

        try:
            user = User.objects.get(pk = pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)

        except User.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        
    if request.method == 'DELETE':
        user = User.objects.get(pk = pk)
        user.delete()
        return Response({'Message': 'User Deleted'})
    
        
    if request.method == 'PUT':
        user = User.objects.get(pk = pk)
        serializer = UserSerializer(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Data': serializer.data,'Message': 'User updated'})