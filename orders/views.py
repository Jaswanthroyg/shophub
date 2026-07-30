from django.db import transaction
from django.db.models import F
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from cart.models import Cart
from .models import Order, OrderItem
from products.models import Product


class CheckoutAPIView(APIView):

    def post(self, request):

        cart_items = Cart.objects.filter(
            user=request.user
        ).select_related("product")

        if not cart_items:
            return Response(
                {"message": "Cart is empty."},
                status=status.HTTP_400_BAD_REQUEST
            )

        with transaction.atomic():

            # Step 1: Validate stock
            for cart_item in cart_items:

                if cart_item.quantity > cart_item.product.stock:
                    return Response(
                        {
                            "message": f"{cart_item.product.name} has only {cart_item.product.stock} items left."
                        },
                        status=status.HTTP_400_BAD_REQUEST
                    )

            # Step 2: Create Order
            order = Order.objects.create(
                user=request.user
            )

            total_amount = 0

            # Step 3: Process each cart item
            for cart_item in cart_items:

                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    price=cart_item.product.price
                )

                Product.objects.filter(
                    id=cart_item.product.id
                ).update(
                    stock=F("stock") - cart_item.quantity
                )

                total_amount += (
                    cart_item.product.price *
                    cart_item.quantity
                )

            order.total_amount = total_amount
            order.save()

            cart_items.delete()

        return Response(
            {
                "message": "Order placed successfully."
            },
            status=status.HTTP_201_CREATED
        )