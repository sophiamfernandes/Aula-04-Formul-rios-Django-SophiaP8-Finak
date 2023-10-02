from django.db import models


class lugares(models.Model):
  cidade=models.CharField(max_length=30)
  pais=models.CharField(max_length=30)
  continente=models.CharField(max_length=30)
  clima=models.CharField(max_length=20)

class coisasEssencias(models.Model):
  IMPORTANCIA=[
    ("M","muito"),
    ("R","medio"),
    ("P","pouco"),
  ]
  cidade=models.CharField(max_length=30)
  artefato=models.CharField(max_length=50)
  importancia=models.CharField(max_length=1,choices=IMPORTANCIA)
  preco=models.IntegerField()
  