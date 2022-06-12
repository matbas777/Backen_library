from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.


class MyAccountManager(BaseUserManager):

    def create_user(self, e_mail, username, password=None):
        if not e_mail:
            raise ValueError("Uzytkownik musi podac adres e-mail")
        if not username:
            raise ValueError("Uzytkownik musi podac nazwe uzytkownika")
        user = self.model(
            e_mail=self.normalize_email(e_mail),
            username=username,
        )
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser):
    username = models.CharField(max_length=264)
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    e_mail = models.EmailField(max_length=264)
    data_joined = models.DateTimeField(auto_now=True)

    objects = MyAccountManager()

    USERNAME_FIELD = 'e_mail'
    REQUIRED_FIELDS = 'username'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


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


