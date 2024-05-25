from django.contrib import admin
from .models import Item, Order

@admin.register(Item)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at', 'updated_at')
    
    
@admin.register(Order)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('items', 'created_at', 'updated_at')
    
    def items(self, obj):
        return ', '.join([i.name for i in obj.items.all()])
