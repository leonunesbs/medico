from django.db import models
from django.utils import timezone


class Agenda(models.Model):
    colaborador = models.ForeignKey(
        'colaboradores.Colaborador', on_delete=models.CASCADE, related_name='agendas')
    horario = models.DateTimeField()

    def __str__(self) -> str:
        return f'{self.horario.strftime("%d/%m/%Y (%H:%M)")} | {self.colaborador}'
