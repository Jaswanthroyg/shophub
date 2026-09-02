from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from .models import Product
from django.db.models import Q
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from .pagination import ProductPagination


class ProductCreateAPIView(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request):

        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ProductListAPIView(APIView):
    def get(self,request):
        search=request.query_params.get("search")
        brand=request.query_params.get("brand")
        products=Product.objects.all()
        #search
        if search:
            products=products.filter(
                Q(name__icontains=search)|
                Q(description__icontains=search)
            )
        #brand filter
        if brand:
            products=products.filter(
                brand__iexact=brand
            )
        #price filter
        min_price=request.query_params.get("min_price")
        max_price=request.query_params.get("max_price")
        if min_price:
            products=products.filter(
                price__gte=min_price
            )
        if max_price:
            products=products.filter(
                price__lte=max_price
            )
        #Pagination
        paginator=ProductPagination()
        page=paginator.paginate_queryset(
            products,
            request
        )
        serializer=ProductSerializer(
            page,
            many=True
        )
        return paginator.get_paginated_response(
            serializer.data
            )

class ProductDetailAPIView(APIView):
    def get(self,request,id):
        product=get_object_or_404(Product,id=id)
        serializer=ProductSerializer(product)
        return Response(serializer.data)

    
class ProductUpdateAPIView(APIView):
    permission_classes = [IsAdminUser]
    def put(self,request,id):
        product=get_object_or_404(Product,id=id)
        serializer=ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class ProductDeleteAPIVIew(APIView):
    permission_classes = [IsAdminUser]
    def delete(self,request,id):
        product=get_object_or_404(Product,id=id)
        product.delete()
        return Response({"message":"Product deleted successfully"},status=status.HTTP_204_NO_CONTENT)