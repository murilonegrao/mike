from django.shortcuts import render
from .models import TrainingSession, SessionExercise

# Create your views here.
def sessions(request):
    sessions = TrainingSession.objects.all().order_by("-performed_at")
    context = {
        'sessions': sessions,
        }

    return render(request, 'sessions.html', context)


def training_session_detail(request, id):
    session = TrainingSession.objects.get(id=id)
    exercises = (
        session.session_exercises
        .select_related('exercise')
        .prefetch_related('exercise_sets')
        .order_by('order'))
    context = {
        'session': session,
        'exercises': exercises,
        }

    return render(request, 'training_session.html', context)

