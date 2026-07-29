from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from .models import Cart
from .serializers import AddToCartSerializer,CartSerializer,UpdateCartSerializer
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

class CartListAPIView(APIView):

    def get(self, request):

        cart_items = cart_items = Cart.objects.filter(
    user=request.user
).select_related("product")

        serializer = CartSerializer(cart_items, many=True)

        return Response(serializer.data)

class UpdateCartAPIView(APIView):
    def patch(self,request,pk):
        serializer=UpdateCartSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cart=get_object_or_404(Cart,id=pk,user=request.user)
        Cart.quantity=serializer.validated_data["quantity"]
        cart.save()
        return Response({"message":"Cart Updated Successfully."},status=status.HTTP_200_OK)
    
class RemoveCartAPIView(APIView):

    def delete(self, request, pk):

        cart = get_object_or_404(
            Cart,
            id=pk,
            user=request.user
        )

        cart.delete()

        return Response(
            {"message": "Product removed from cart successfully."},
            status=status.HTTP_200_OK
        )