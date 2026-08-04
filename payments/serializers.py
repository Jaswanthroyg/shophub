from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields="__all__"
        read_only_fields=[
            "amount",
            "status",
            "payment_method",
            "gateway_payment_id",
            "created_at"
        ]
class VerifyPaymentSerializer(serializers.Serializer):
    razorpay_order_id=serializers.CharField()
    razorpay_payment_id=serializers.CharField()
    razorpay_signature=serializers.CharField()

    
