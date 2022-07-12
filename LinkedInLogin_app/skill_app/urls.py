# LinkedInLogin_app/urls.py
from django.urls import path, include

from .views import Home # new

urlpatterns = [
path("accounts/", include("allauth.urls")),
path("", Home.as_view(), name="home"), # new
]