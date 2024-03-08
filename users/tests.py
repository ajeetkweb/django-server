from django.test import TestCase, Client
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory

from users.serializers import UserSerializer

from users.models import User
from users import views


# Create your tests here.

class UserTest(TestCase):

    def setUp(self) -> None:

        User.objects.create(name ="Sanju", age = 25, gender='Female')
        User.objects.create(name ="Kittu", age = 10, gender='Male')

    
    def test_get_user(self):
        user1 = User.objects.get(name ='Sanju')
        user2 = User.objects.get(name ='Kittu')
        self.assertEqual(user1.getUser(), user1.name)
        self.assertEqual(user2.getUser(), user2.name)

    def test_get_all_users(self):

        client = Client()
        # get API response
        response = client.get(reverse('list-users'))

        # get data from DB
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
    def test_create_user(self):

        client = APIClient()

        input_data = {
        "name": "Abhi kkk",
        "age": 24,
        "gender": "Male"
        }

        res = client.post(reverse('create-user'), data=input_data)
        self.assertEqual(res.data['name'], 'Abhi kkk')
        self.assertEqual(res.status_code, 201)

    def test_post_user(self):

        input_data = {
        "name": "Amitkumar",
        "age": 24,
        "gender": "Male"
        }

        factory = APIRequestFactory()
        request = factory.post(reverse('create-user'), input_data, format='json')
        response = views.create_user(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    
    def test_get_single_user(self):

        mohan = User.objects.create(name ="Mohan", age = 30, gender='Male')
        client = APIClient()
        response = client.get(reverse('single-user'), args= {'pk' :mohan.pk})

        user = User.objects.get(pk=mohan.pk)
        serializer = UserSerializer(user)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_get_invalid_user(self):

        client = APIClient()

        response = client.get(reverse('single-user'), args={'pk': 30})
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

        










        


        

        
       





