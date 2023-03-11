from django.db import models

class Livro(models.Model):
    nome = models.CharField(max_length=60)
    finalizado = models.BooleanField(default=False)
    resenha = models.TextField(max_length=450)

    def __str__(self) -> str:
        return self.nome
   