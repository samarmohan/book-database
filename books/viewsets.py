from .models import BookResponse
from rest_framework import generics
from .serializers import BookResponseSerializer


class BookResponseCreate(generics.CreateAPIView):
    queryset = BookResponse.objects.all()
    serializer_class = BookResponseSerializer
    lookup_field = "Title"


class BookResponseGet(generics.ListAPIView):
    queryset = BookResponse.objects.all()
    serializer_class = BookResponseSerializer
    lookup_field = "Title"


class BookResponseRetrieveSingle(generics.RetrieveAPIView):
    queryset = BookResponse.objects.all()
    serializer_class = BookResponseSerializer
    lookup_field = "Title"


class BookResponseUpdate(generics.RetrieveUpdateAPIView):
    queryset = BookResponse.objects.all()
    serializer_class = BookResponseSerializer
    lookup_field = "Title"


class BookResponseDelete(generics.RetrieveDestroyAPIView):
    queryset = BookResponse.objects.all()
    serializer_class = BookResponseSerializer
    lookup_field = "Title"
