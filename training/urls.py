from django.urls import path
from . import views

app_name = 'training'

urlpatterns = [
    path('', views.training_session_list, name='training_session_list'),
    path('session/new/', views.training_session_create, name='training_session_create'),
    path('session/<int:pk>/', views.training_session_detail, name='training_session_detail'),
    path('session/<int:pk>/edit/', views.training_session_update, name='training_session_update'),
    path('session/<int:pk>/delete/', views.training_session_delete, name='training_session_delete'),
    path('session-exercise/<int:pk>/', views.session_exercise_detail, name='session_exercise_detail'),
    path('session-exercise/<int:session_exercise_pk>/sets/<int:pk>/edit/', views.exercise_set_update, name='exercise_set_update'),
    path('session-exercise/<int:session_exercise_pk>/sets/<int:pk>/delete/', views.exercise_set_delete, name='exercise_set_delete'),
]
