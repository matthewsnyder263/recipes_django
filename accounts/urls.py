from django.urls import path
from accounts.views import signup
# from . import views

urlpatterns = [
    path("signup/", signup, name="signup")
]
