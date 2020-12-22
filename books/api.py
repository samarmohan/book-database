from .models import BookResponse
from rest_framework import generics
from .serializers import BookResponseSerializer


class CreateAPI(generics.CreateAPIView):
    queryset = BookResponse.objects.all()
    serializer_class = BookResponseSerializer
    lookup_field = "Title"


class ListAPI(generics.ListAPIView):
    queryset = BookResponse.objects.all()
    serializer_class = BookResponseSerializer
    lookup_field = "Title"


class RetrieveAPI(generics.RetrieveAPIView):
    queryset = BookResponse.objects.all()
    serializer_class = BookResponseSerializer
    lookup_field = "Title"


class UpdateAPI(generics.RetrieveUpdateAPIView):
    queryset = BookResponse.objects.all()
    serializer_class = BookResponseSerializer
    lookup_field = "Title"


class DeleteAPI(generics.RetrieveDestroyAPIView):
    queryset = BookResponse.objects.all()
    serializer_class = BookResponseSerializer
    lookup_field = "Title"
