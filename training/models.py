from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class TrainingSession(models.Model):
    SESSION_TYPES = [
        ('UPPER','UPPER'),
        ('LOWER','LOWER'),
        ('PULL','PULL'),
        ('PUSH','PUSH'),
        ('FULLBODY','FULLBODY'),
    ]

    performed_at = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='training_sessions'
    )
    
    session_type = models.CharField(
        max_length=20,
        choices=SESSION_TYPES,
        blank=True,
        null=True
    )
    
    def __str__(self):
        t = self.session_type or "NO_TYPE"
        return f"{self.performed_at:%Y-%m-%d %H:%M} - {t}"


class Exercise(models.Model):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=120, unique=True)

    def __str__(self):
        return str(self.name)


class SessionExercise(models.Model):
    VARIATIONS = [
        ('DUMBBELL', 'DUMBBELL'),
        ('BARBELL', 'BARBELL'),
        ('MACHINE', 'MACHINE'),
        ('BODYWEIGHT', 'BODYWEIGHT'),
        ('OTHER', 'OTHER'),
    ]

    order = models.PositiveSmallIntegerField()
    session = models.ForeignKey(
        TrainingSession,
        on_delete=models.CASCADE,
        related_name='session_exercises',
        )
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        related_name='appearances'
        )
    variation = models.CharField(
        max_length=20,
        choices=VARIATIONS,
    )


class ExerciseSet(models.Model):
    order = models.PositiveSmallIntegerField()
    session_exercise = models.ForeignKey(
        SessionExercise,
        on_delete=models.CASCADE,
        related_name='exercise_sets',
    )
    reps = models.PositiveSmallIntegerField(blank=True, null=True)
    duration = models.PositiveSmallIntegerField(blank=True, null=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True)
