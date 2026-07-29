from rest_framework import serializers
from .models import Cart
from products.models import Product

class AddToCartSerializer(serializers.Serializer):
    product=serializers.IntegerField()

class ProductCartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "price",
            "image"
        ]

class CartSerializer(serializers.ModelSerializer):

    product = ProductCartSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = [
            "id",
            "product",
            "quantity"
        ]

