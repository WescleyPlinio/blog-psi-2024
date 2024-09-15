from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=350)
    conteudo = models.TextField(max_length=2000, default='default_value')
    carac = models.TextField(max_length=250, default='default_value')
    imagem = models.ImageField(upload_to='static/imgs')
    dt_postagem = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo