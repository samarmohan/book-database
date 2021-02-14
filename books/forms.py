from django import forms
from .models import BookModel


# Fields in form represented in create and update pages
class BookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = [
            "Title",
            "Author",
            "Description",
            "PageCount",
            "GradeLevel",
            "Rating"
        ]
