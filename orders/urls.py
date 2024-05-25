from django.urls import path
from .views import  ItemListView, ItemDetailView, OrderCreateView, OrderDetailAPIView, UserOrdersView

urlpatterns = [
    path('items/', ItemListView.as_view(), name='item_list'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('orders/', OrderCreateView.as_view(), name='order_create'),
    path('orders/<int:pk>/', OrderDetailAPIView.as_view(), name='order_detail'),
    path('user/orders/', UserOrdersView.as_view(), name='user_orders'),
]