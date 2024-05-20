from django.urls import path

from . import views

urlpatterns = [
    path("landing", views.ListUsers.as_view(), name="index"),
]