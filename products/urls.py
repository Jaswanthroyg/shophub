from django.urls import path 
from .views import ProductCreateAPIView, ProductListAPIView


urlpatterns=[
    path("create/",ProductCreateAPIView.as_view(),name="product-create"),
    path("",ProductListAPIView.as_view(),name="product-List")
]