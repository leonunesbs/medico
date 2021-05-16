from django.db import models


class Paciente(models.Model):
    user = models.ForeignKey(
        'users.User', on_delete=models.SET_NULL, null=True, blank=True, related_name='paciente')
    nome_completo = models.CharField(max_length=100)
    data_de_nascimento = models.DateField()

    def __str__(self) -> str:
        return self.nome_completo
