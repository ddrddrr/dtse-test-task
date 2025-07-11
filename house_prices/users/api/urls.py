from django.urls import path
from knox.views import LogoutView, LogoutAllView
from users.api.views import LoginView, RegistrationView

urlpatterns = [
    path(r"register/", RegistrationView.as_view(), name="register"),
    path(r"login/", LoginView.as_view(), name="knox_login"),
    path(r"logout/", LogoutView.as_view(), name="knox_logout"),
    path(r"logoutall/", LogoutAllView.as_view(), name="knox_logoutall"),
]
