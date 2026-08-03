from django.urls import path

from .views import CreatePaymentAPIView


urlpatterns = [
    path(
        "",
        CreatePaymentAPIView.as_view(),
        name="create-payment",
    ),
]