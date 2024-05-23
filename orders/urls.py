from django.urls import path
from .views import  ItemListView, ItemDetailView, OrderCreateView, OrderDetailAPIView

urlpatterns = [
    path('items/', ItemListView.as_view(), name='item_list'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('orders/', OrderCreateView.as_view(), name='order_create'),
    path('orders/<int:pk>/', OrderDetailAPIView.as_view(), name='order_detail'),
]