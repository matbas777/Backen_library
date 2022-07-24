from datetime import timedelta, datetime

from rest_framework import serializers

from library.models import Book, User, Borrower


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id", "book_title", "author_name")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "e_mail", "password")


class AuthenticationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
        )


class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = ("id", "book", "user", "date_of_delivery", "is_returned")


class ReturnedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        filter = "is_returned"


class NewBorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = ("id", "book", "date_of_delivery", "is_returned")

    def validate(self, quantity):
        person = quantity.get("user")
        if Borrower.objects.filter(user=person, is_returned=False).count() == 5:
            raise serializers.ValidationError(
                "nie mozesz wypoczyc wiecej niz 5 ksiazek. oddaj ksiazke aby moc wypoczycyc kolejna"
            )
        bookk = quantity.get("book")
        if Borrower.objects.filter(book=bookk, is_returned=False):
            raise serializers.ValidationError(
                "nie mozna wypozyczyc ksiazki jest ona juz wypozyczona"
            )
        date_of_delivery = quantity.get("date_of_delivery")
        if date_of_delivery > datetime.today().date() + timedelta(days=30):
            raise serializers.ValidationError(
                "Nie mozesz wypozyczyc ksizki wiecej niz na 30 dni"
            )
        return quantity
