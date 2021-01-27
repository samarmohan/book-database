from django import forms
from .models import BookModel


class BookForm(forms.ModelForm):
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
