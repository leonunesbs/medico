from django.db import models


class Paciente(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=100)
    data_de_nascimento = models.DateField()
