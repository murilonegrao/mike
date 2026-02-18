from urllib import request
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def manuals_index(request):
    return render(request, 'pages/manuals_index.html')

def manual_claude(request):
    return render(request, 'pages/manual_claude.html')

def manual_deepseek(request):
    return render(request, 'pages/manual_deepseek.html')

def manual_gemini(request):
    return render(request, 'pages/manual_gemini.html')

def manual_manus(request):
    return render(request, 'pages/manual_manus.html')

def manual_chatgpt(request):
    return render(request, 'pages/manual_chatgpt.html')
