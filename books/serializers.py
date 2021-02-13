from rest_framework import serializers
from .models import BookModel


# Serializer for DRF
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookModel
        fields = ("Name", "Email", "Title", "Author", "Description", "PageCount", "Rating")
