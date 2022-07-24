from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    GenericAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from library.models import Book, User, Borrower
from library.serializers import (
    BookSerializer,
    UserSerializer,
    BorrowerSerializer,
    ReturnedSerializer,
    NewBorrowerSerializer,
    AuthenticationUserSerializer,
)
import jwt, datetime


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


class RegisterUserAPIView(APIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        instance.set_password(serializer.validated_data.get("password"))
        instance.save()
        return Response()


class LoginUserView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get("e_mail")
        password = request.data.get("password")

        user = User.objects.filter(e_mail=email).first()

        if user is None:
            raise AuthenticationFailed("Dane sa nieprawidlowe")

        if not user.check_password(password):
            raise AuthenticationFailed("Dane sa nieprawidlowe")

        payload = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            "iat": datetime.datetime.utcnow(),
        }

        token = jwt.encode(payload, "secret", algorithm="HS256")

        response = Response()

        response.set_cookie(key="jwt", value=token, httponly=True)
        response.data = {"jwt": token}

        return response


class UserView(APIView):
    def get(self, request, *args, **kwargs):
        token = request.COOKIES.get("jwt")

        if not token:
            raise AuthenticationFailed("Uzytkownik nieuwierzytelniony")

        try:
            payload = jwt.decode(token, "secret", algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Uzytkownik nieuwierzytelniony")

        user = User.objects.filter(id=payload["id"]).first()
        serializer = AuthenticationUserSerializer(user)
        return Response(serializer.data)


class LogoutUserView(APIView):
    def get(self, request, *args, **kwargs):
        response = Response()
        response.delete_cookie("jwt")
        response.data = {"message": "Wylogowany"}
        return response


class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.COOKIES.get("jwt")

        if not token:
            raise AuthenticationFailed("Uzytkownik nieuwierzytelniony")

        try:
            payload = jwt.decode(token, "secret", algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Uzytkownik nieuwierzytelniony")


class CreateBorrowerAPIView(APIView):
    authentication_classes = (APIKeyAuthentication,)

    def post(self, request, *args, **kwargs):
        token = request.COOKIES.get("jwt")
        payload = jwt.decode(token, "secret", algorithms=["HS256"])
        user = User.objects.filter(id=payload["id"]).first()
        serializer = NewBorrowerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        borrower = Borrower(user=user, **serializer.validated_data).save()

        return Response()
