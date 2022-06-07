from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView

from library.models import Book, User, Borrower
from library.serializers import BookSerializer, UserSerializer, BorrowerSerializer, ReturnedSerializer, \
    NewBorrowerSerializer


class BookListAPIView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BorrowerListAPIView(ListAPIView):
    serializer_class = BorrowerSerializer
    queryset = Borrower.objects.all()


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ReturnedAPIView(UpdateAPIView):
    serializer_class = ReturnedSerializer
    queryset = Borrower.objects.all()


class CreateUserAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CreateBorrowerAPIView(CreateAPIView):
    serializer_class = NewBorrowerSerializer
    queryset = Borrower.objects.all()