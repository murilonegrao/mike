from django.urls import path
from . import views

urlpatterns = [
    path('', views.sessions, name='home'),
]
