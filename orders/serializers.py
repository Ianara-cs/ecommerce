from rest_framework import serializers
from .models import Item, Order

class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Item
        fields = ('id', 'name', 'price', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')
        extra_kwargs = {
            'name': {'required': True},
            'price': {'required': True},
        }
    
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("O preço não pode ser negativo.")
        return value

class OrderSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'items', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')
        
    def validate(self, data):
        if not data.get('items'):
            raise serializers.ValidationError("A lista de itens não pode estar vazia.")

        return data