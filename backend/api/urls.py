from django.urls import path

from users.views import LoginView, RegisterUser
from documents.views import upload_pdf

urlpatterns = [
    path("create-user/", RegisterUser, name="create-user"),
    path("login/", LoginView, name="login"),
    path("upload/", upload_pdf, name="upload"),
]
