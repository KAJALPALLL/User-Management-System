from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User

class UserAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            "first_name": "Test",
            "last_name": "User",
            "company_name": "Test Corp",
            "age": 25,
            "city": "Test City",
            "state": "TS",
            "zip": 12345,
            "email": "testuser@example.com",
            "web": "http://testuser.com"
        }
        self.user = User.objects.create(**self.user_data)

    # Test Case for fetching the list of users
    def test_get_all_users(self):
        response = self.client.get("/api/users")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("data", response.data)

    # Test Case for adding the user
    def test_create_user(self):
        new_user_data = self.user_data.copy()
        new_user_data["email"] = "new@example.com"
        response = self.client.post("/api/users", new_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # Test Case for update the user
    def test_update_user(self):
        payload = {"first_name": "First Name","last_name":"Last Name", "age": 30}
        response = self.client.put(f"/api/users/{self.user.id}", payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test Case for delete the user
    def test_delete_user(self):
        response = self.client.delete(f"/api/users/{self.user.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(User.objects.filter(id=self.user.id).exists())
