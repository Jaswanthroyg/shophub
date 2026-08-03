from django.urls import path 
from .views import ProductCreateAPIView, ProductDeleteAPIVIew, ProductListAPIView,ProductDetailAPIView, ProductUpdateAPIView


urlpatterns=[
    path("create/",ProductCreateAPIView.as_view(),name="product-create"),
    path("",ProductListAPIView.as_view(),name="product-List"),
    path("<int:id>/",ProductDetailAPIView.as_view(),name="product-detail"),
    path("<int:id>/",ProductUpdateAPIView.as_view(),name="product-update"),
    path("<int:id>/",ProductDeleteAPIVIew.as_view(),name="product-delete"),
]
