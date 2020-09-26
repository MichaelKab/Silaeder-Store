from django.urls import path

from . import views

urlpatterns = [
    path("x", views.main, name='x'),
]