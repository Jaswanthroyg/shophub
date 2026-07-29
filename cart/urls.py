from django.urls import path
from .views import AddToCartAPIView,CartListAPIView


urlpatterns=[
    path("add/",AddToCartAPIView.as_view(),name="add-to-cart"),
    path("",CartListAPIView.as_view(),name="cart-list")
]