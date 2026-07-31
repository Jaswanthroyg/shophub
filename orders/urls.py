from django.urls import path
from .views import CheckoutAPIView,OrderListAPIView,OrderDetailView


urlpatterns=[
    path("checkout/",CheckoutAPIView.as_view(),name="checkout"),
    path("",OrderListAPIView.as_view(),name="order_list"),
    path("<int:pk>/",OrderDetailView.as_view(),name="order_detail")
]