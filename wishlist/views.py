from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Wishlist
from .serializers import WishlistSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from products.models import Product
from django.shortcuts import get_object_or_404

class WishlistAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
            wishlist_items = Wishlist.objects.filter(
                user=request.user
            ).select_related("product")
            serializer = WishlistSerializer(
                wishlist_items,
                many=True
            )
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

    def post(self, request):

        product_id = request.data.get("product")

        if not product_id:
            return Response(
                {"message": "Product is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        product = get_object_or_404(
            Product,
            id=product_id
        )

        wishlist, created = Wishlist.objects.get_or_create(
            user=request.user,
            product=product
        )

        if not created:
            return Response(
                {"message": "Product is already in wishlist."},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = WishlistSerializer(wishlist)

        return Response(
            {
                "message": "Product added to wishlist.",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )
    def delete(self,request,pk):
         wishlist_item=get_object_or_404(
              Wishlist,
              id=pk,
              user=request.user
         )
         wishlist_item.delete()
         return Response(
              {"message":"product removed from wishlist"},
              status=status.HTTP_200_OK
         )