from rest_framework import serializers
from .models import Order,OrderItem


class OrderListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order

        fields = [
            "id",
            "total_amount",
            "status",
            "created_at"
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
    