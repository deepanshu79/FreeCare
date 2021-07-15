from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("predict", views.predict, name="predict"),
    path("details/", views.details, name="details"),
    path("hospitals/", views.location, name="hospitals")
]
