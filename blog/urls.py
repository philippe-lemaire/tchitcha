from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:slug>/",
        views.ArticleDetailView.as_view(),
        name="detail",
    ),
]
