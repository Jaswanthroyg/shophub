from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class AuthenticationTests(APITestCase):

    def test_user_registration(self):
        data = {
            "username": "jaswanth",
            "email": "jaswanth@test.com",
            "password": "Test@12345"
        }

        response = self.client.post("/api/accounts/register/", data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        self.client.post("/api/accounts/register/", {
            "username": "jaswanth",
            "email": "jaswanth@test.com",
            "password": "Test@12345"
        })

        response = self.client.post("/api/accounts/login/", {
            "username": "jaswanth",
            "password": "Test@12345"
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)