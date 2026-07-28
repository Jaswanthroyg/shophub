from django.db import models


class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField(default=0)
    brand=models.CharField(max_length=100)
    category=models.ForeignKey("categories.Category", on_delete=models.CASCADE, related_name="products")
    image=models.ImageField(upload_to="product_images/", null=True, blank=True)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
