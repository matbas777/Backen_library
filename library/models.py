from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    e_mail = models.EmailField


class Book(models.Model):
    book_title = models.CharField(max_length=300)
    author_name = models.CharField(max_length=200)


class Borrower(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_delivery = models.DateField
    is_returned = models.BooleanField(default=False)


