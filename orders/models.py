from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Order(models.Model):

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Confirmed", "Confirmed"),
        ("Shipped", "Shipped"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="orders"
    )

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id}"

class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.product.name}"

class OrderAddress(models.Model):
    order=models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        related_name="delivery_address"
    )
    full_name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=15)
    address_line_1=models.CharField(max_length=255)
    address_line_2=models.CharField(
        max_length=255,
        blank=True
    )
    street=models.CharField(max_length=255)
    landmark=models.CharField(max_length=255,
                              blank=True)
    village=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    district=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.CharField(max_length=10)
    country=models.CharField(
        max_length=100,
        default="India"
    )
    def __str__(self):
        return f"Address for Order #{self.order.id}"
