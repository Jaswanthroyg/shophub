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
        model = Order
        fields = ["status"]

    def validate_status(self, value):

        current_status = self.instance.status

        allowed_transitions = {
            "Pending": ["Confirmed", "Cancelled"],
            "Confirmed": ["Shipped", "Cancelled"],
            "Shipped": ["Delivered"],
            "Delivered": [],
            "Cancelled": [],
        }

        if value not in allowed_transitions[current_status]:
            raise serializers.ValidationError(
                f"Cannot change order status from "
                f"{current_status} to {value}."
            )

        return value
