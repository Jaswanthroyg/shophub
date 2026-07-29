from django.urls import path
from .views import AddToCartAPIView,CartListAPIView,UpdateCartAPIView


urlpatterns=[
    path("add/",AddToCartAPIView.as_view(),name="add-to-cart"),
    path("",CartListAPIView.as_view(),name="cart-list"),
    path("<int:pk>/", UpdateCartAPIView.as_view(), name="update-cart"),
]