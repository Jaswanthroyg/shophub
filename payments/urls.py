from django.urls import path

from .views import PaymentVerifyAPIView


urlpatterns = [
    path("verify/", PaymentVerifyAPIView.as_view(), name="payment-verify"),
]