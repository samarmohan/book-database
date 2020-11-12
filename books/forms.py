from django import forms
from .models import BookResponse


class BookResponseForm(forms.ModelForm):
    class Meta:
        model = BookResponse
        fields = [
            "Name",
            "Email",
            "Title",
            "Author",
            "Description",
            "Rating"
        ]