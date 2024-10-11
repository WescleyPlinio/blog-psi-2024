from django.db import models

class Caracteristica(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(max_length=350)


class Post(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=350)
    conteudo = models.TextField(max_length=2000, default='default_value')
    carac = models.ForeignKey(Caracteristica, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='static/imgs')
    dt_postagem = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo