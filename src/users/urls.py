from django.urls import path

from users.views import SignUpView, SignInView, logout_view, home


urlpatterns = [
    path("", home, name="user-home"),
    path("sign-up/", SignUpView.as_view(), name="user-sign-up"),
    path("sign-in/", SignInView, name="user-sign-in"),
    path("sign-out/", logout_view, name="user-sign-out"),
]
