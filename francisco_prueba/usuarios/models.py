from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Registro(models.Model):
    #vvariables para el modelo
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Registro')
    date_register = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date_register']

    def __str__(self):
        return f'{self.user.username}: {self.date_register}' #formato para mostrar en administrador