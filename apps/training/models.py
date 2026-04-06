from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
from django.core.exceptions import ValidationError

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
        default=''
    )
    
    def __str__(self):
        t = self.session_type or "NO_TYPE"
        return f"{self.performed_at:%Y-%m-%d %H:%M} - {t}"


class Exercise(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    def clean(self):
        super().clean()

        if not self.slug:
            self.slug = slugify(self.name)

        if not self.slug:
            raise ValidationError({'name':'Nome inválido para gerar slug'})
        
        qs = Exercise.objects.filter(slug=self.slug)
        if self.pk:
            qs = qs.exclude(pk=self.pk)
        
        if qs.exists():
            raise ValidationError({"name": "Já existe um exercício com esse nome (slug duplicado)."})
    
    def save(self, *args, **kwargs):
        self.full_clean()        
        super().save(*args, **kwargs)

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
        on_delete=models.PROTECT,
        related_name='appearances'
        )
    variation = models.CharField(
        max_length=20,
        choices=VARIATIONS,
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['session', 'order'],
                name='uniq_sessionexercise_order_per_session',
            )
        ]

    def __str__(self):
        return f'{self.session} | {self.order}. {self.exercise} - {self.variation}'


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

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['session_exercise', 'order'],
                name='uniq_exerciseset_order_per_session_exercise',
            )
        ]

    def clean(self):
        super().clean()
        has_reps = self.reps is not None
        has_duration = self.duration is not None
        if has_reps == has_duration:
            raise ValidationError('Preencha reps OU duration (apenas um).')
        
    
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
    
    def __str__(self):
        if self.reps is not None:
            main = f'{self.reps} reps'
        else:
            main = f'{self.duration}s'

        weight = f' @ {self.weight}kg' if self.weight is not None else ''
        return f'{self.order}: {main}{weight}'


