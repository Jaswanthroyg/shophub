from django.urls import path
from .views import CategoryAPIView, CategoryDetailAPIView

urlpatterns = [
    path(
        "",
        CategoryAPIView.as_view(),
        name="category-list-create"
    ),
    path(
        "<int:id>/",
        CategoryDetailAPIView.as_view(),
        name="category-detail"
    ),
]