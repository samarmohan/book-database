from .models import BookResponse
from rest_framework import generics
from .serializers import BookResponseSerializer


class BookResponseCreate(generics.CreateAPIView):
    queryset = BookResponse.objects.all()
    serializer_class = BookResponseSerializer


class BookResponseGet(generics.ListAPIView):
    queryset = BookResponse.objects.all()
    serializer_class = BookResponseSerializer


class BookResponseRetrieveSingle(generics.RetrieveAPIView):
    queryset = BookResponse.objects.all()
    serializer_class = BookResponseSerializer


class BookResponseUpdate(generics.RetrieveUpdateAPIView):
    queryset = BookResponse.objects.all()
    serializer_class = BookResponseSerializer


class BookResponseDelete(generics.RetrieveDestroyAPIView):
    queryset = BookResponse.objects.all()
    serializer_class = BookResponseSerializer
