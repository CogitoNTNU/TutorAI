from django.urls import path

from api.views import hello_world


urlpatterns = [
    path("hello_word", hello_world),
]
