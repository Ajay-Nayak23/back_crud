from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be a positive number.")
        return value

    class Meta:
        model = Item
        fields = '__all__'
