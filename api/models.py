from django.db import models

class Item(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly defining the ID field
    name = models.CharField(max_length=255)  # Name of the item
    category = models.CharField(max_length=100)  # Category (e.g., Electronics, Clothing)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Price of the item
    description = models.TextField(blank=True, null=True)  # Optional description
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when item was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when item was last updated

    def __str__(self):
        return self.name
