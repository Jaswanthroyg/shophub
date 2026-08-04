from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.db import transaction
from django.db.models import F

from cart.models import Cart
from products.models import Product
from orders.models import OrderItem
from .models import Payment
from .serializers import VerifyPaymentSerializer

import razorpay


client = razorpay.Client(
    auth=(
        settings.RAZORPAY_KEY_ID,
        settings.RAZORPAY_KEY_SECRET
    )
)


class PaymentVerifyAPIView(APIView):

    def post(self, request):

        # Step 1: Validate Request
        serializer = VerifyPaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        razorpay_order_id = serializer.validated_data["razorpay_order_id"]
        razorpay_payment_id = serializer.validated_data["razorpay_payment_id"]
        razorpay_signature = serializer.validated_data["razorpay_signature"]

        # Step 2: Find Payment
        payment = get_object_or_404(
            Payment,
            gateway_order_id=razorpay_order_id
        )

        # Step 3: Verify Razorpay Signature
        try:

            client.utility.verify_payment_signature(
                {
                    "razorpay_order_id": razorpay_order_id,
                    "razorpay_payment_id": razorpay_payment_id,
                    "razorpay_signature": razorpay_signature,
                }
            )

        except razorpay.errors.SignatureVerificationError:

            return Response(
                {
                    "message": "Invalid payment signature."
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        # Step 4: Update Database
        with transaction.atomic():

            # Update Payment
            payment.gateway_payment_id = razorpay_payment_id
            payment.status = "Completed"
            payment.save()
            if payment.status == "Completed":
                return Response(
                    {
                        "message": "Payment already verified."
                    },
                    status=status.HTTP_200_OK
                )

            # Update Order
            order = payment.order
            order.status = "Confirmed"
            order.save()

            # Reduce Product Stock
            order_items = OrderItem.objects.filter(
                order=order
            ).select_related("product")

            for item in order_items:

                product = item.product

                if item.quantity > product.stock:

                    return Response(
                    {
                        "message": f"Payment received, but '{product.name}' is out of stock. Refund is required."
                    },
                    status=status.HTTP_409_CONFLICT
                )

            # Clear User Cart
            Cart.objects.filter(
                user=order.user
            ).delete()

        # Step 5: Success Response
        return Response(
            {
                "message": "Payment verified successfully.",
                "order_id": order.id,
                "payment_status": payment.status,
                "order_status": order.status
            },
            status=status.HTTP_200_OK
        )