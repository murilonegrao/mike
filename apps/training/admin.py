from django.contrib import admin
from .models import TrainingSession, Exercise, SessionExercise, ExerciseSet

# Register your models here.
admin.site.register(TrainingSession)
admin.site.register(Exercise)
admin.site.register(SessionExercise)
admin.site.register(ExerciseSet)
