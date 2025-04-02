 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Item
from .serializers import ItemSerializer
from collections import defaultdict


# ✅ GET (List) & POST (Create) → /api/items/
class ItemListView(APIView):
    """
    Handles:
    - GET /api/items/ (List all items with filtering)
    - POST /api/items/ (Create a new item)
    """

    def get(self, request):
        """List all items grouped by category (bucketing) with optional filtering."""
        search_query = request.query_params.get('name', None)
        category_filter = request.query_params.get('category', None)

        queryset = Item.objects.all()

        # Apply filtering
        if search_query:
            queryset = queryset.filter(name__icontains=search_query)
        if category_filter:
            queryset = queryset.filter(category=category_filter)

        # Bucketing: Group items by category
        bucketed_data = defaultdict(list)
        for item in queryset:
            bucketed_data[item.category].append(ItemSerializer(item).data)

        return Response(bucketed_data, status=status.HTTP_200_OK)

    def post(self, request):
        """Create a new item."""
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ✅ GET (Retrieve), PUT (Update), DELETE → /api/items/<id>/
class ItemDetailView(APIView):
    """
    Handles:
    - GET /api/items/<id>/ (Retrieve an item)
    - PUT /api/items/<id>/ (Update an item)
    - DELETE /api/items/<id>/ (Delete an item)
    """

    def get(self, request, pk):
        """Retrieve a single item by ID."""
        item = get_object_or_404(Item, id=pk)
        serializer = ItemSerializer(item)

        bucketed_data = defaultdict(list)
        bucketed_data[item.category].append(ItemSerializer(item).data)
        return Response(bucketed_data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        """Update an existing item."""
        item = get_object_or_404(Item, id=pk)
        serializer = ItemSerializer(item, data=request.data, partial=False)  # Full update
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Delete an item."""
        item = get_object_or_404(Item, id=pk)
        item.delete()
        return Response({"message": "Item deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

 