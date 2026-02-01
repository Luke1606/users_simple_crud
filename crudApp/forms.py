from .models import Persona
from django import forms

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'