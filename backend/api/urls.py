from django.urls import path

from users.views import login, register_user
from documents.views import upload_pdf

urlpatterns = [
    path("create-user/", register_user, name="create-user"),
    path("login/", login, name="login"),
    path("upload/", upload_pdf, name="upload"),
]
