from django.urls import path

from . import views

urlpatterns = [
    path("users", views.ListUsers.as_view(), name="index"),
]