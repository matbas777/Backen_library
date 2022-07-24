from unittest.mock import ANY

import pytest
from django.test import TestCase

from rest_framework.test import APIClient
# Create your tests here.
from library.models import User

client = APIClient()

@pytest.mark.django_db
def test_RegisterUserAPIView():
    number = User.objects.count()
    response = client.post('/registration', data={
        "username": "Bobes12",
        "first_name": "Mateusz",
        "last_name": "Kowalski",
        "e_mail": "kowalski.mateusz1234@gmail.com",
        "password": "Kochamksiazki@123"
    })
    assert response.status_code == 200
    assert User.objects.count() == number + 1



@pytest.mark.django_db
def test_LoginUserView():
    user = User.objects.create(**{
        "username": "Bobes12",
        "first_name": "Mateusz",
        "last_name": "Kowalski",
        "e_mail": "kowalski.mateusz1234@gmail.com",
    })
    user.set_password("Kochamksiazki@123")
    user.save()
    jwt = client.post('/login', data={
        "e_mail": "kowalski.mateusz1234@gmail.com",
        "password": "Kochamksiazki@123"
                                      })
    assert jwt.json() == {"jwt": ANY}

    wrong_password = client.post('/login', data={
        "e_mail": "kowalski.mateusz1234@gmail.com",
        "password": "Kochamksiazki"})
    assert wrong_password.status_code == 403
    assert wrong_password.json().get('detail') == "Dane sa nieprawidlowe"

@pytest.mark.django_db
def test_LogoutUserView():
    logout_user = client.get('/logout')
    assert logout_user.json().get('message') == "Wylogowany"
