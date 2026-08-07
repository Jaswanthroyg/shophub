from django.db import models
from django.conf import settings


class Address(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,
                           on_delete=models.CASCADE,
                           related_name='addresses')
    full_name=models.CharField(
        max_length=100)
    
    phone_number=models.CharField(
        max_length=15
    )

    address_line_1=models.CharField(
        max_length=255,
        blank=True
    )
    address_line_2=models.CharField(
        max_length=255,
        blank=True
    )

    street=models.CharField(
        max_length=255
    )

    village=models.CharField(
        max_length=255
    )

    city=models.CharField(
        max_length=100
    )
    district=models.CharField(
        max_length=100
    )

    state=models.CharField(
        max_length=100
    )
    pincode=models.CharField(
        max_length=10
    )
    country=models.CharField(
        max_length=100,
        default='India'
    )
    landmark=models.CharField(
        max_length=255,
        blank=True
    )
    is_default=models.BooleanField(
        default=False)
    created_at=models.DateTimeField(
        auto_now_add=True   
    )
    updated_at=models.DateTimeField(
        auto_now=True
    )
    def __str__(self):
        return f"{self.name} - {self.city}"

