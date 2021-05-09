from django.db import models


class Consulta(models.Model):
    paciente = models.ForeignKey(
        'pacientes.Paciente', on_delete=models.CASCADE)
    agenda = models.ForeignKey(
        'agenda.Agenda', on_delete=models.SET_NULL, blank=True, null=True)
    anamnese = models.TextField()
    exame_fisico = models.TextField()
