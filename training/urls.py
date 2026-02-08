from django.urls import path
from . import views

urlpatterns = [
    path('', views.sessions, name='home'),
    path('session/<int:id>/', views.training_session_detail, name='training_session')
]
