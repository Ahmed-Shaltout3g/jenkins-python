from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('product/create/', views.ProductCreateView.as_view(), name='product-create'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('product/update/<int:pk>/', views.ProductUpdateView.as_view(), name='product-update'),
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product-delete'),
]
