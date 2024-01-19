from django.db import models
from django.contrib.auth.models import User
class Categoria(models.Model):
  nome= models.CharField( max_length=20)
  
  def __str__(self):
    return self.nome
class Flashcard(models.Model):
  DIFICULDADE_CHOICE=(('D', 'Dificil')('M','Médio')("F")("Facil"))
  user= models.ForeignKey(User, on_delete=models.DO_NOTHING)
  pergunta=models.CharField(max_length=100)
  resposta=models.TextField()
  Categoria=models.ForeignKey(Categoria,on_delete=models.DO_NOTHING)
  dificuldade=models.CharField(max_length=1,choices=DIFICULDADE_CHOICE)
  def __str__(self):
    return self.pergunta