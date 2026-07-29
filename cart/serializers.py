from rest_framework import serializers

class AddToCartSerializer(serializers.Serializer):
    product=serializers.IntegerField()
