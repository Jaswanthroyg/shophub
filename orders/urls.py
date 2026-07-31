from django.urls import path
from .views import CheckoutAPIView,OrderListAPIView,OrderDetailView,CancelOrderAPIView


urlpatterns=[
    path("checkout/",CheckoutAPIView.as_view(),name="checkout"),
    path("",OrderListAPIView.as_view(),name="order_list"),
    path("<int:pk>/",OrderDetailView.as_view(),name="order_detail"),
    path("<int:pk>/cancel/",CancelOrderAPIView.as_view(),name="cancel-order")
]