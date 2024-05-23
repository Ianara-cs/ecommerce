from rest_framework import generics 
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from .models import Item, Order
from .serializers import ItemSerializer, OrderSerializer


class ItemListView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class OrderCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def perform_create(self, serializer):
        serializer.save()
        
    def create(self, request, *args, **kwargs):
        items_data = request.data.get('items', [])
        order_serializer = self.get_serializer(data=request.data)

        if order_serializer.is_valid():
            order_instance = order_serializer.save()

            for item_data in items_data:
                item_id = item_data.get('id')
                try:
                    item = Item.objects.get(pk=item_id)
                    order_instance.items.add(item)  
                except ObjectDoesNotExist:
                    return Response({'error': f'Item com ID {item_id} não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

            headers = self.get_success_headers(order_serializer.data)
            return Response(order_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetailAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

