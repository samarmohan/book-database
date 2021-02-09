from django.urls import path
from .views import home_view, BookCreateView, BookDetailView, BookUpdateView

urlpatterns = [
    path('add-book/', BookCreateView.as_view()),
    path('<Title>/update/', BookUpdateView.as_view()),
    path('<Title>/detail/', BookDetailView.as_view()),
    path('', home_view),
]
