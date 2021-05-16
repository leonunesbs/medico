from django.db import models


class Unidade(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome
