from django.db import transaction
from django.db.models import F
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated,IsAdminUser

from cart.models import Cart
from .models import Order, OrderItem
from products.models import Product
from .serializers import OrderListSerializer,OrderDetailSerializer,OrderStatusUpdateSerializer


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

class OrderListAPIView(APIView):
    def get(self,request):
        orders=Order.objects.filter(
            user=request.user
        ).order_by("created_at")

        serializer=OrderListSerializer(orders, many=True)
        return Response(serializer.data)

class OrderDetailView(APIView):
    def get(self,request,pk):
        order=get_object_or_404(Order.objects.prefetch_related("items__product"),
                                id=pk,
                                user=request.user
                                )
        serializer=OrderDetailSerializer(order)
        return Response(serializer.data)

class CancelOrderAPIView(APIView):
    permission_classes=[IsAuthenticated]
    def patch(self,request,pk):
        order=get_object_or_404(
            Order,
            id=pk,
            user=request.user
        )
        if order.status in [
            "shipped",
            "delivered",
            "cancelled"
        ]:
            return Response({
                "error":"This order can not be cancelled."
            },status=status.HTTP_400_BAD_REQUEST)
        order.status="cancelled"
        order.save()
        return Response({
            "message":"Order Cancelled Successfully."
        },status=status.HTTP_200_OK)

class OrderStatusUpdateAPIView(APIView):

    permission_classes = [IsAdminUser]

    def patch(self, request, pk):

        order = get_object_or_404(
            Order,
            id=pk
        )

        serializer = OrderStatusUpdateSerializer(
            order,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                {
                    "message": "Order status updated successfully.",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )