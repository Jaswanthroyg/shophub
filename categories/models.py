from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='category_images/')
    is_active=models.BooleanField(default=True)

