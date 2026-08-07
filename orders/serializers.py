from rest_framework import serializers
from .models import Order,OrderItem,OrderAddress

class OrderAddressSerializer(serializers.ModelSerializer):

    class Meta:
        model= OrderAddress
        fields= "__all__"
class OrderListSerializer(serializers.ModelSerializer):
    delivery_address = OrderAddressSerializer(
        read_only=True
    )

    class Meta:
        model = Order

        fields = [
            "id",
            "total_amount",
            "status",
            "created_at",
            "delivery_address"
        ]
class OrderItemSerializer(serializers.ModelSerializer):
    product=serializers.CharField(
        source="product.name",
        read_only=True
    )
    class Meta:
        model=OrderItem
        fields=[
            "product",
            "quantity",
            "price"
        ]
class OrderDetailSerializer(serializers.ModelSerializer):
    items=OrderItemSerializer(many=True,read_only=True)
    class Meta:
        model=Order
        fields=[
            "id",
            "status",
            "total_amount",
            "created_at",
            "items"
        ]
class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields=["status"]

