import django_filters

from books.models import BookModel


ORDERING_CHOICES = (
    ("asc", "Lowest Ratings First"),
    ("desc", "Highest Ratings First"),
)


class BookFilter(django_filters.FilterSet):
    ordering = django_filters.ChoiceFilter(label="Ordering", choices=ORDERING_CHOICES, method="filter_by_order")

    class Meta:
        model = BookModel
        fields = {
            "Title": ["icontains"],
            "Author": ["icontains"],
            "Name": ["icontains"],
            "GradeLevel": ["exact"]
        }

    @staticmethod
    def filter_by_order(queryset, name, value):
        expression = "Rating" if value == "asc" else "-Rating"
        return queryset.order_by(expression)
