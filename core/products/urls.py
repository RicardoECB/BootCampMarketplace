from django.urls import path
from .views import (
    ProtectedView, ProductListAPIView, ProductCreateAPIView,
    PhotoListAPIView, PhotoCreateAPIView,
    TagListAPIView, TagCreateAPIView,
    CategoryListAPIView, CategoryCreateAPIView,
)

urlpatterns = [
    path('protected/', ProtectedView.as_view(), name = 'protected'),
    path('products/', ProductListAPIView.as_view(), name='product-list'),
    path('products/create/', ProductCreateAPIView.as_view(), name='product-create'),
    path('photos/', PhotoListAPIView.as_view(), name='photo-list'),
    path('photos/create/', PhotoCreateAPIView.as_view(), name='photo-create'),
    path('tags/', TagListAPIView.as_view(), name='tag-list'),
    path('tags/create/', TagCreateAPIView.as_view(), name='tag-create'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('categories/create/', CategoryCreateAPIView.as_view(), name='category-create'),
]
