from django import forms
from .models import TrainingSession, SessionExercise, ExerciseSet


class MikeFormMixin:
    """
    Aplica classes Bootstrap + Mike automaticamente nos widgets.
    Mantém compatível com {{ form.as_p }} (sem precisar renderizar campo a campo manualmente).
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            w = field.widget

            if isinstance(w, (forms.Select, forms.SelectMultiple)):
                w.attrs["class"] = (w.attrs.get("class", "") + " form-select m-input").strip()
                continue

            if isinstance(w, forms.CheckboxInput):
                w.attrs["class"] = (w.attrs.get("class", "") + " form-check-input").strip()
                continue

            w.attrs["class"] = (w.attrs.get("class", "") + " form-control m-input").strip()
                

class TrainingSessionForm(MikeFormMixin,forms.ModelForm):
    class Meta:
        model = TrainingSession
        fields = [
            'performed_at',
            'session_type',
            'description',
        ]
        labels = {
            'performed_at': 'Data',
            'session_type': 'Tipo de treino',
            'description': 'Descrição',
        }
        widgets = {
            'performed_at': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and getattr(self.instance, "pk", None) and "performed_at" in self.fields:
            val = getattr(self.instance, "performed_at", None)
            if val:
                try:
                    self.initial["performed_at"] = val.date()
                except Exception:
                    self.initial["performed_at"] = val


        if "session_type" in self.fields:
            self.fields["session_type"].widget.attrs.setdefault("placeholder", "Ex.: Treino A")

        if "description" in self.fields:
            self.fields["description"].widget.attrs.setdefault("placeholder", "Opcional: foco do treino, notas, etc.")

class SessionExerciseForm(MikeFormMixin, forms.ModelForm):
    class Meta:
        model = SessionExercise
        fields = [
            'exercise',
            'variation',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if "variation" in self.fields:
            self.fields["variation"].widget.attrs.setdefault("placeholder", "Ex.: Barra, Halteres, Máquina...")


class ExerciseSetForm(MikeFormMixin, forms.ModelForm):
    class Meta:
        model = ExerciseSet
        fields = [
            'duration',
            'reps',
            'weight',
            'description',
        ]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if "duration" in self.fields:
            self.fields["duration"].widget = forms.NumberInput(attrs={
                "class": "form-control m-input", 
                "inputmode": "numeric",
                "min":"0",
                "step": "1",
                "placeholder": "Tempo em segundos",
            })
        
        if "reps" in self.fields:
            self.fields["reps"].widget = forms.NumberInput(attrs={
                "class": "form-control m-input",
                "inputmode": "numeric",
                "min": "0",
                "step": "1",
                "placeholder": "Reps",
            })

        if "weight" in self.fields:
            self.fields["weight"].widget = forms.NumberInput(attrs={
                "class": "form-control m-input",
                "inputmode": "decimal",
                "min": "0",
                "step": "0.5",
                "placeholder": "Carga (kg)",
            })

        if "description" in self.fields:
            self.fields["description"].widget.attrs.setdefault("placeholder", "Opcional: RPE, observações, etc.")

print("MRO TrainingSessionForm:", [c.__name__ for c in TrainingSessionForm.mro()])