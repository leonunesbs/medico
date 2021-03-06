from django.db import models


class Colaborador(models.Model):
    user = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, related_name='colaborador')
    nome_completo = models.CharField(max_length=100)
    ocupacao = models.CharField(max_length=100)
    registro = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Colaboradores'

    def __str__(self) -> str:
        return self.nome_completo
