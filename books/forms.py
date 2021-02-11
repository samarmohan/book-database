from django import forms
from .models import BookModel


class BookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = [
            "Title",
            "Author",
            "Description",
            "PageCount",
            # "GradeLevel",
            "Rating"
        ]
