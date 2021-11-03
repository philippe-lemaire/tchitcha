from django.urls import path
from django.views.generic import DetailView
from . import views
from .models import Movie

app_name = "movies"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", DetailView.as_view(model=Movie), name="detail"),
]
