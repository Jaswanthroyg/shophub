from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status

from products.models import Product
from categories.models import Category
from addresses.models import Address
from cart.models import Cart


User = get_user_model()


class OrderTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="ordertest",
            email="ordertest@example.com",
            password="Test@12345"
        )

        self.client.force_authenticate(user=self.user)

        self.category = Category.objects.create(
            name="Test Category"
        )

        self.product = Product.objects.create(
            name="Test Product",
            description="Test product description",
            price=100,
            stock=10,
            brand="Test Brand",
            category=self.category
        )

        self.address = Address.objects.create(
            user=self.user,
            full_name="Test User",
            phone_number="9876543210",
            address_line_1="Main Road",
            address_line_2="Near Temple",
            street="Main Street",
            village="Test Village",
            city="Test City",
            district="Test District",
            state="Andhra Pradesh",
            pincode="522000",
            country="India",
            landmark="Near Temple",
            is_default=True
        )

    def test_checkout_requires_address(self):
        Cart.objects.create(
            user=self.user,
            product=self.product,
            quantity=1
        )

        response = self.client.post(
            "/api/orders/checkout/",
            {}
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_order_list_requires_authentication(self):
        self.client.force_authenticate(user=None)

        response = self.client.get(
            "/api/orders/"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )