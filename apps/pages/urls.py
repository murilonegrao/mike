from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='home'),
    path('manuals_index/', views.manuals_index, name='manuals_index'),
    path('manual_claude/', views.manual_claude, name='manual_claude'),
    path('manual_deepseek/', views.manual_deepseek, name='manual_deepseek'),
    path('manual_gemini/', views.manual_gemini, name='manual_gemini'),
    path('manual_manus/', views.manual_manus, name='manual_manus'),
    path('manual_chatgpt/', views.manual_chatgpt, name='manual_chatgpt'),
]
