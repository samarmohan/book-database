from .models import BookModel
from rest_framework import generics
from .serializers import BookSerializer


class CreateAPI(generics.CreateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    lookup_field = "Title"


class ListAPI(generics.ListAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    lookup_field = "Title"


class RetrieveAPI(generics.RetrieveAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    lookup_field = "Title"


class UpdateAPI(generics.RetrieveUpdateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    lookup_field = "Title"


class DeleteAPI(generics.RetrieveDestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    lookup_field = "Title"
