from rest_framework import serializers
from .models import BookResponse


class BookResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookResponse
        fields = ("Name", "Email", "Title", "Author", "Summary", "PageCount", "ContainsBadWords", "Rating")
