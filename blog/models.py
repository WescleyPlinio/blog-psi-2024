from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=350)
    subtitulo = models.CharField(max_length=50)
    conteudo = models.TextField(max_length=2000)

