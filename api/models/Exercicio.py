from django.db import models


class Exercicio(models.Model):
    
    class Meta:
        db_table = 'EXERCICIO'
    
    nome = models.CharField(max_length=100)
    repeticoes = models.IntegerField()
    series = models.IntegerField()
    descanso = models.IntegerField()
    musculo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
