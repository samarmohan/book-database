from django import forms
from .models import BookModel


class BookForm(forms.ModelForm):
    ContainsBadWords = forms.BooleanField(label="Is this book inappropriate for someone around 8 years old?")

    class Meta:
        model = BookModel
        fields = [
            "Name",
            "Email",
            "Title",
            "Author",
            "Description",
            "PageCount",
            "ContainsBadWords",
            "Rating"
        ]
