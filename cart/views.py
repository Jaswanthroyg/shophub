from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from .models import Cart
from .serializers import AddToCartSerializer
from products.models import Product


class AddToCartAPIView(APIView):
    

    def post(self, request):

        serializer = AddToCartSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        product = get_object_or_404(
            Product,
            id=serializer.validated_data["product"]
        )

        cart, created = Cart.objects.get_or_create(
            user=request.user,
            product=product,
            defaults={
                "quantity": 1
            }
        )

        if not created:
            cart.quantity += 1
            cart.save()

        return Response(
            {
                "message": "Product added to cart successfully."
            },
            status=status.HTTP_200_OK
        )