from django.db import models

# Create your models here.


class User(models.Model):

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    e_mail = models.EmailField(max_length=354, null=True)


class Book(models.Model):

    def __str__(self):
        return self.book_title

    book_title = models.CharField(max_length=300)
    author_name = models.CharField(max_length=200)


class Borrower(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_delivery = models.DateField(null=True)
    is_returned = models.BooleanField(default=False)


