from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Payment
from .serializers import PaymentSerializer,VerifyPaymentSerializer



class PaymentVerifyAPIView(APIView):
    def post(self,request,):
        serializer=VerifyPaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        razorpay_order_id = serializer.validated_data["razorpay_order_id"]
        razorpay_Payment_id=serializer.validated_data["razorpay_payment_id"]
        razorpay_signature=serializer.validated_data["razorpay_signature"]

        payment=get_object_or_404(
            Payment,
            gateway_order_id=razorpay_order_id
        )