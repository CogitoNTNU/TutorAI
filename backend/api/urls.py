from django.urls import path

from api.views import hello_world
from users.views import CreateUserView

urlpatterns = [
    path("hello_word", hello_world),
    path("create-user/", CreateUserView.as_view(), name="create-user"),
]
