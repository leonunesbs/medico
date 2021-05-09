from django.db import models


class Agenda(models.Model):
    colaborador = models.ForeignKey(
        'colaboradores.Colaborador', on_delete=models.CASCADE)
    horario = models.DateTimeField()
