from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from .models import Payment
from .serializers import PaymentSerializer
from .models import Order
import razorpay
from django.conf import settings


Client=razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,
                             settings.RAZORPAY_KEY_SECRET
                             ))

class CreatePaymentAPIView(APIView):
    def post(self,request):
        serializer=PaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        order=serializer.validated_data["order"]
        
        payment=Payment.objects.create(
            order=order,
            amount=order.total_amount
        )
        if Payment.objects.filter(order=order).exists():
            return Response(
                {"message":"Payment already exists for this order."},
                status=status.HTTP_400_BAD_REQUEST
            )
        