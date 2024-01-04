from django.urls import path

from api.views import hello_world
from users.views import LoginView, RegisterUser

urlpatterns = [
    path("hello_word", hello_world),
    path("create-user/", RegisterUser, name="create-user"),
    path("login/", LoginView, name="login"),
]
