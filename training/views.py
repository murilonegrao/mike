from django.shortcuts import render
from .models import TrainingSession, SessionExercise

# Create your views here.
def sessions(request):
    sessions = TrainingSession.objects.all()
    context = {
        'sessions': sessions,
        }

    return render(request, 'sessions.html', context)