from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from .models import TrainingSession, SessionExercise
from .forms import TrainingSessionForm, SessionExerciseForm

# Create your views here.
def sessions(request):
    sessions = (
        TrainingSession.objects
        .all()
        .annotate(
            exercise_count=Count('session_exercises', distinct=True),
            set_count=Count('session_exercises__exercise_sets', distinct=True),
        )   
        .order_by("-performed_at")
    )
    context = {
        'sessions': sessions,
        }

    return render(request, 'sessions.html', context)


def training_session_detail(request, id):
    session = get_object_or_404(TrainingSession, id=id)
    exercises_qs = (
        session.session_exercises
        .select_related('exercise')
        .prefetch_related('exercise_sets')
        .order_by('order')
        )
    
    if request.method == 'POST':
        form = SessionExerciseForm(request.POST)
        if form.is_valid():
            se = form.save(commit=False)
            se.session = session
            se.order = exercises_qs.count() +1
            se.save()
            return redirect('training_session_detail', id=session.id)
    else:
        form = SessionExerciseForm()


    context = {
        'session': session,
        'exercises': exercises_qs,
        'form': form,
        }

    return render(request, 'training_session.html', context)


def training_session_create(request):
    if request.method =='POST':
        form = TrainingSessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user
            session.save()
            return redirect('training_session_detail', id=session.id)
    else:
        form = TrainingSessionForm()

    return render(request, 'new_session.html', {'form': form})