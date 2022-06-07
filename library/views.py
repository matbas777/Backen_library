from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView

from library.models import Book
from library.serializers import BookSerializer


class BookListAPIView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()