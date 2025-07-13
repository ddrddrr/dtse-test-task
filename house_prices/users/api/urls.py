from django.urls import path
from users.api.views import LoginView, RegistrationView

urlpatterns = [
    path(r"register/", RegistrationView.as_view(), name="register"),
    path(r"login/", LoginView.as_view(), name="login"),
]
