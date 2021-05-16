from django.db import models
from django.utils import timezone


class Consulta(models.Model):
    unidade = models.ForeignKey(
        'unidades.Unidade', on_delete=models.SET_NULL, null=True, related_name='consultas')
    paciente = models.ForeignKey(
        'pacientes.Paciente', on_delete=models.CASCADE, related_name='consultas')
    agenda = models.ForeignKey(
        'agenda.Agenda', on_delete=models.SET_NULL, blank=True, null=True, related_name='consulta')
    anamnese = models.TextField()
    exame_fisico = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.last_update = timezone.now()
        super(Consulta, self).save(*args, **kwargs)
