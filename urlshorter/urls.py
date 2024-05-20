
from django.urls import path

from . import views

urlpatterns = [
    path("shortner", views.URLListView.as_view(), name="index"),
    path("redirect", views.URLRedirect.as_view(), name="index"),
]