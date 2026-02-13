from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, Max
from .models import TrainingSession, SessionExercise, ExerciseSet
from .forms import TrainingSessionForm, SessionExerciseForm, ExerciseSetForm

# Create your views here.
def training_session_list(request):
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

    return render(request, 'training_session_list.html', context)


def training_session_detail(request, pk):
    session = get_object_or_404(TrainingSession, pk=pk)
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
            se.order = exercises_qs.count() + 1
            se.save()
            return redirect('training_session_detail', pk=session.pk)
    else:
        form = SessionExerciseForm()


    context = {
        'session': session,
        'exercises': exercises_qs,
        'form': form,
        }

    return render(request, 'training_session_detail.html', context)


def training_session_create(request):
    if request.method =='POST':
        form = TrainingSessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.user = request.user
            session.save()
            return redirect('training_session_detail', pk=session.pk)
    else:
        form = TrainingSessionForm()

    return render(request, 'training_session_form.html', {'form': form})


def session_exercise_detail(request, pk):
    se = get_object_or_404(
        SessionExercise.objects.select_related('session', 'exercise'),
        pk=pk
    )

    sets_qs = se.exercise_sets.all().order_by('order')

    if request.method == 'POST':
        form = ExerciseSetForm(request.POST)
        if form.is_valid():
            s = form.save(commit=False)
            s.session_exercise = se

            max_order = se.exercise_sets.aggregate(Max('order'))['order__max'] or 0
            s.order = max_order + 1

            s.save()
            return redirect('training:session_exercise_detail', pk=se.pk)
        
    else:
        form = ExerciseSetForm()

    return render(
        request,
        'session_exercise_detail.html',
        {'se': se, 'sets': sets_qs, 'form': form}
    )


@login_required
def session_exercise_update(request, session_exercise_pk, pk):
    session_exercise = get_object_or_404(
        SessionExercise,
        pk=session_exercise_pk,
        session__user=request.user,
    )

    exercise_set = get_object_or_404(
        ExerciseSet,
        pk=pk,
        session_exercise=session_exercise,
    )

    if request.method == 'POST':
        form = ExerciseSetForm(request.POST, instance=exercise_set)
        if form.is_valid():
            form.save()
            return redirect('training:session_exercise_detail', pk=session_exercise_pk)
    else:
        form = ExerciseSetForm(instance=exercise_set)

    return render(
        request,
        'exercise_set_form.html',
        {
            'session_exercise': session_exercise,
            'exercise_set': exercise_set,
            'form': form,
        },
    )


@login_required
def session_exercise_delete(request, session_exercise_pk, pk):
    session_exercise = get_object_or_404(
        SessionExercise,
        pk=session_exercise_pk,
        session__user=request.user,
    )

    exercise_set = get_object_or_404(
        ExerciseSet,
        pk=pk,
        session_exercise=session_exercise,
    )

    if request.method == 'POST':
        exercise_set.delete()
        remaining = ExerciseSet.objects.filter(session_exercise=session_exercise).order_by('order')
        for idx, s in enumerate(remaining, start=1):
            if s.order != idx:
                s.order = idx
                s.save(update_fields=['order'])
        return redirect('training:session_exercise_detail', pk=session_exercise.pk)

    return render(
        request,
        'exercise_set_confirm_delete.html',
        {
            'session_exercise': session_exercise,
            'exercise_set': exercise_set,
        },
    )


