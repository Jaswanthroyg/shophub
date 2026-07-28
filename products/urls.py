from django.urls import path 
from .views import ProductCreateAPIView


urlpatterns=[
    path("create/",ProductCreateAPIView.as_view(),name="product-create"),
]