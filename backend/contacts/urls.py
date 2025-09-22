from django.urls import path
from . import views

urlpatterns = [
    path("api/savecontact/", views.save_contact, name="save_contact"),
]