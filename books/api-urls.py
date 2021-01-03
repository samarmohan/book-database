from django.urls import path
from books.api import CreateAPI, ListAPI, RetrieveAPI, UpdateAPI, DeleteAPI

urlpatterns = [
    path('create/', CreateAPI.as_view()),
    path('', ListAPI.as_view()),
    path('<Title>/detail/', RetrieveAPI.as_view()),
    path('<Title>/update/', UpdateAPI.as_view()),
    path('<Title>/delete/', DeleteAPI.as_view()),
]
