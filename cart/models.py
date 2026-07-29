from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Cart(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="cart_items"
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="cart_items"
    )

    quantity = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "product"],
                name="unique_user_product"
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"