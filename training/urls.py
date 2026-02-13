from django.urls import path
from . import views

app_name = 'training'

urlpatterns = [
    path('', views.training_session_list, name='training_session_list'),
    path('session/new/', views.training_session_create, name='training_session_create'),
    path('session/<int:pk>/', views.training_session_detail, name='training_session_detail'),
    path('session-exercise/<int:pk>/', views.session_exercise_detail, name='session_exercise_detail'),
    path('session-exercise/<int:session_exercise_pk>/sets/<int:pk>/edit', views.session_exercise_update, name='exercise_set_update'),
    path('session-exercise/<int:session_exercise_pk>/sets/<int:pk>/delete', views.session_exercise_delete, name='exercise_set_delete'),
]
