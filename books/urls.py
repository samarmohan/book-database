from django.urls import path
from .views import BookListView, BookCreateView, BookDetailView, BookUpdateView

urlpatterns = [
    path('add-book/', BookCreateView.as_view(), name="create"),
    path('<Title>/update/', BookUpdateView.as_view(), name="update"),
    path('<Title>/detail/', BookDetailView.as_view(), name="detail"),
    path('', BookListView.as_view(), name="home"),
]
