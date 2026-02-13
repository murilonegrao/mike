from django import forms
from .models import TrainingSession, SessionExercise, ExerciseSet

class TrainingSessionForm(forms.ModelForm):
    class Meta:
        model = TrainingSession
        fields = [
            'performed_at',
            'session_type',
            'description',
        ]

class SessionExerciseForm(forms.ModelForm):
    class Meta:
        model = SessionExercise
        fields = [
            'exercise',
            'variation',
        ]


class ExerciseSetForm(forms.ModelForm):
    class Meta:
        model = ExerciseSet
        fields = [
            'duration',
            'reps',
            'weight',
            'description',
        ]

