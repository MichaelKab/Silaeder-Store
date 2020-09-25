from django.urls import path
from . import views

urlpatterns = [
    path("x", views.Main, name='x'),
    #path('logs', views.Session_log_v(request,ID=1), name='logs'),

]