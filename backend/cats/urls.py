from django.urls import path
from . import views

urlpatterns = [
    path("api/showcat/<int:pk>/", views.show_cat, name="show_cat"),
]