
# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

User = get_user_model()


class UserAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user(self):
        """Test creating a new user"""
        payload = {
            'email': 'test@example.com',
            'password': 'testpass',
            'first_name': 'John',
            'last_name': 'Doe',
            # Add other required fields here
        }
        response = self.client.post('/api/users/create/', payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        # Add additional assertions for other fields if necessary

    def test_retrieve_user(self):
        """Test retrieving a user"""
        user = User.objects.create_user(
            email='test@example.com',
            password='testpass',
            first_name='John',
            last_name='Doe',
            # Add other required fields here
        )
        self.client.force_authenticate(user=user)

        response = self.client.get('/api/users/retrieve/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], user.email)
        # Add additional assertions for other fields if necessary

    # Add more tests for other views (UpdateUserView, ListUserView, etc.) if needed

    def test_authenticate_user(self):
        """Test authenticating a user"""
        User.objects.create_user(
            email='test@example.com',
            password='testpass',
            first_name='John',
            last_name='Doe',
            # Add other required fields here
        )
        payload = {
            'email': 'test@example.com',
            'password': 'testpass',
        }
        response = self.client.post('/api/users/token/', payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        # Add additional assertions if necessary
