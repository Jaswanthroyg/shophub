from django.urls import path
from .views import WishlistAPIView

urlpatterns=[
    path("",WishlistAPIView.as_view(),name="wishlist"),
    path("<int:pk>/",WishlistAPIView.as_view(),name="wishlist_delete"),
    

]