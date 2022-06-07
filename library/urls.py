from django.urls import path

from library import views

urlpatterns = [
    path('books', views.BookListAPIView.as_view(), name=''),
    path('get_book', views.CreateBorrowerAPIView.as_view(), name=''),
    path('new_user', views.CreateUserAPIView.as_view(), name=''),
    path('user', views.UserListAPIView.as_view(), name=''),
]

