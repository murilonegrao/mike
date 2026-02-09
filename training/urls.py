from django.urls import path
from . import views

urlpatterns = [
    path('', views.sessions, name='session_list'),
    path('session/new/', views.training_session_create, name='training_session_create'),
    path('session/<int:id>/', views.training_session_detail, name='training_session_detail'),
]
