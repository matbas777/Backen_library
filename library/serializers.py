from rest_framework import serializers

from library.models import Book, User, Borrower


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            "id",
            "book_title",
            "author_name"
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "e_mail"
        )


class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = (
            "id",
            "book",
            "user",
            "date_of_delivery"
        )