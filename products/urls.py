from django.urls import path 
from .views import ProductCreateAPIView, ProductDeleteAPIVIew, ProductListAPIView,ProductDetailAPIView, ProductUpdateAPIView


urlpatterns=[
    path("create/",ProductCreateAPIView.as_view(),name="product-create"),
    path("",ProductListAPIView.as_view(),name="product-List"),
    path("<int:id>/",ProductDetailAPIView.as_view(),name="product-detail"),
    path("<int:id>/update/",ProductUpdateAPIView.as_view(),name="product-update"),
    path("<int:id>/delete/",ProductDeleteAPIVIew.as_view(),name="product-delete"),
]
