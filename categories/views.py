from django. shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import CategorySerializer
from .models import Category

class CategoryAPIView(APIView):

    def get(self, request):

        categories = Category.objects.all()

        serializer = CategorySerializer(
            categories,
            many=True
        )

        return Response(serializer.data)

    def post(self, request):

        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
class CategoryDetailAPIView(APIView):
    def get(self,request,id):
        category=get_object_or_404(Category,id=id)
        serializer=CategorySerializer(category)
        return Response(serializer.data)
    
    def put(self,request,id):
        category=get_object_or_404(Category,id=id)
        serializer=CategorySerializer(instance=category,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({ "message": "Category updated successfully", "data": serializer.data })
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        category=get_object_or_404(Category,id=id)
        category.delete()
        return Response(
    {
        "message": "Category deleted successfully."
    },
    status=status.HTTP_200_OK
)