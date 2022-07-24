from django.urls import path

from library import views

urlpatterns = [
    path("books", views.BookListAPIView.as_view(), name=""),
    path("get_book", views.CreateBorrowerAPIView.as_view(), name=""),
    path("registration", views.RegisterUserAPIView.as_view(), name=""),
    path("find_user", views.UserView.as_view(), name=""),
    path("login", views.LoginUserView.as_view(), name=""),
    path("logout", views.LogoutUserView.as_view(), name=""),
    path("auth_user", views.UserView.as_view(), name=""),
]
