from datetime import datetime
from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class Persona(models.Model):
    ci = models.CharField(primary_key=True, max_length=11, unique=True, validators=[
        RegexValidator(r'^\d{11}$', message='El numero debe ser de 11 dígitos.'),
    ])
    name = models.CharField(max_length=30, blank=False)  # No se puede dejar vacío
    email = models.EmailField(blank=False)  # No se puede dejar vacío
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"La persona de nombre: {self.name}, con correo: {self.email} y se unio el dia {self.joined_date}."

    def clean(self):
        super().clean()
        self.validate_birthdate()

    def validate_birthdate(self):
        # Valida que los 6 primeros dígitos del ID sean una fecha válida.
        birthdate = self.ci[:6]
        try:
            birthdate = datetime.strptime(birthdate, '%y%m%d')
        except ValueError as exc:
            raise ValidationError('Los primeros 6 dígitos deben ser una fecha valida') from exc
