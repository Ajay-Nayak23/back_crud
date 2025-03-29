from django.contrib import admin
from .models import Item  # Import the Item model

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'description', 'created_at', 'updated_at')  # Show all fields in the list view
    search_fields = ('name', 'category')  # Enables search functionality
    list_filter = ('category', 'created_at')  # Adds filters for category and creation date
    ordering = ('-created_at',)  # Orders items by most recent first
    readonly_fields = ('created_at', 'updated_at')  # Makes timestamps non-editable
