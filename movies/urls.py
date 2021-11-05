from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("film/<int:pk>/", views.MovieDetailView.as_view(), name="detail"),
    path("<int:pk>/", views.ShowingDetailView.as_view(), name="showing_detail"),
    path("billeterie/<int:showing_id>", views.buy_tickets, name="buy_tickets"),
]
