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

        # Prevent duplicate verification
        if payment.status == "Completed":
            return Response(
                {
                    "message": "Payment already verified."
                },
                status=status.HTTP_200_OK
            )

        # Step 3: Verify Signature
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

        # Step 4: Fetch Payment Details from Razorpay
        payment_details = client.payment.fetch(
            razorpay_payment_id
        )

        # Step 5: Update Database
        with transaction.atomic():

            # Update Payment
            payment.gateway_payment_id = razorpay_payment_id
            payment.payment_method = payment_details["method"].upper()
            payment.status = "Completed"
            payment.save()

            # Update Order
            order = payment.order
            order.status = "Confirmed"
            order.save()

            # Reduce Stock
            order_items = OrderItem.objects.filter(
                order=order
            ).select_related("product")

            for item in order_items:

                product = item.product

                # Check stock again
                if item.quantity > product.stock:

                    return Response(
                        {
                            "message": f"Payment received, but '{product.name}' is out of stock. Refund required."
                        },
                        status=status.HTTP_409_CONFLICT
                    )

                Product.objects.filter(
                    id=product.id
                ).update(
                    stock=F("stock") - item.quantity
                )

            # Clear Cart
            Cart.objects.filter(
                user=order.user
            ).delete()

        # Step 6: Success Response
        return Response(
            {
                "message": "Payment verified successfully.",
                "order_id": order.id,
                "payment_status": payment.status,
                "payment_method": payment.payment_method,
                "order_status": order.status
            },
            status=status.HTTP_200_OK
        )