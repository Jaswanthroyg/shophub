from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=(
        "id",
        "name",
        "price",
        "stock",
        "brand",
        "category",
        "is_active",

    )
    search_fields=(
        "name",
        "brand"
    )
    list_filter=(
        "is_active",
        "category",
        "brand"
    )
