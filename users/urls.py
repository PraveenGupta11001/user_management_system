# users/urls.py

from django.urls import path, include
from users.views import dashboard, register, logoutView


urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path('dashboard/', dashboard, name="dashboard"),
    path('', dashboard, name="dashboard"),
    path("register/", register, name="register"),
    path("logout/", logoutView, name="logout"),
]