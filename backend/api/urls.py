from django.urls import path

from users.views import LoginView, RegisterUser

urlpatterns = [
    path("create-user/", RegisterUser, name="create-user"),
    path("login/", LoginView, name="login"),
]
