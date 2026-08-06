from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields = [
                "id",
                "full_name",
                "phone_number",
                "address_line_1",
                "street",
                "area",
                "city",
                "district",
                "state",
                "pincode",
                "country",
                "landmark",
                "is_default",
                "created_at",
                "updated_at",
        ]
    read_only_fields=['user',
                      'created_at',
                      'updated_at',
                      'is_default'
                      ]