from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.db import transaction

from .models import Address
from .serializers import AddressSerializer


class AddressListCreateAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        addresses = Address.objects.filter(
            user=request.user
        )

        serializer = AddressSerializer(
            addresses,
            many=True
        )

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request):

        serializer = AddressSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        is_first_address = not Address.objects.filter(
            user=request.user
        ).exists()

        serializer.save(
            user=request.user,
            is_default=is_first_address
        )

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

class AddressDetailAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, user, pk):

        return get_object_or_404(
            Address,
            id=pk,
            user=user
        )

    def get(self, request, pk):

        address = self.get_object(
            request.user,
            pk
        )

        serializer = AddressSerializer(address)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def put(self, request, pk):

        address = self.get_object(
            request.user,
            pk
        )

        serializer = AddressSerializer(
            address,
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def patch(self, request, pk):

        address = self.get_object(
            request.user,
            pk
        )

        serializer = AddressSerializer(
            address,
            data=request.data,
            partial=True
        )

        serializer.is_valid(
            raise_exception=True
        )

        serializer.save()

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def delete(self, request, pk):

        address = self.get_object(
            request.user,
            pk
    )

        was_default = address.is_default

        address.delete()

        if was_default:

             new_default = Address.objects.filter(
            user=request.user
        ).first()

        if new_default:

            new_default.is_default = True
            new_default.save()

        return Response(
        {
            "message": "Address deleted successfully."
        },
        status=status.HTTP_200_OK
    )

class SetDefaultAddressAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        address = get_object_or_404(
            Address,
            id=pk,
            user=request.user
        )

        with transaction.atomic():

            Address.objects.filter(
                user=request.user,
                is_default=True
            ).update(
                is_default=False
            )

            address.is_default = True
            address.save()

        return Response(
            {
                "message": "Default address updated successfully."
            },
            status=status.HTTP_200_OK
        )