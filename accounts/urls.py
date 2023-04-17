from django.urls import path
from accounts.views import signup, user_login, user_logout
# from . import views

urlpatterns = [
    path("logout/", user_logout, name="user_logout"),
    path("login/", user_login, name="user_login"),
    path("signup/", signup, name="signup")
]
