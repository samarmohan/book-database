from django.urls import path
from .views import home_view, add_book_view, update_view, detail_view

urlpatterns = [
    path('add-book/', add_book_view),
    path('<title>/update/', update_view),
    path('<title>/detail/', detail_view),
    path('', home_view),
]
