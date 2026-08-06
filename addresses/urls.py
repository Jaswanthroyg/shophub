from django.urls import path

from addresses.views import AddressListCreateAPIView,AddressDetailAPIView,SetDefaultAddressAPIView


urlpatterns = [
    path(
        "",
        AddressListCreateAPIView.as_view(),
        name="address-list-create"
    ),
    path(
        "<int:pk>/",
        AddressDetailAPIView.as_view(),
        name="address-detail"
    ),
      path(
        "<int:pk>/set-default/",
        SetDefaultAddressAPIView.as_view(),
        name="set-default-address"
    ),

    ]
