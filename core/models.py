from django.db import models
from tinymce import models as tinymce_models


class Cargo(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=120)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.name


class Autor(models.Model):
    name = models.CharField(max_length=20, verbose_name='Nome')
    second_name = models.CharField(max_length=80, verbose_name='Segundo nome')
    birthDt = models.DateField(verbose_name='Data de Aniversário')
    email = models.EmailField(verbose_name='Email')
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, verbose_name='Cargo')

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.name


class Post(models.Model):
    themes = (
        ('geek', 'Geek'),
        ('politic', 'Política'),
        ('curious', 'Curiosidades'),
    )
    status_post = (
        ('racunho', 'Rascunho'),
        ('publicado', 'Publicado'),
        ('arquivado', 'Arquivado'),
    )

    title = models.CharField(max_length=100, verbose_name='Título')
    sub_title = models.CharField(max_length=200, verbose_name='Subtítulo')
    content = tinymce_models.HTMLField()
    status = models.CharField(max_length=9, default='rascunho', choices=status_post, blank=False, null=False, verbose_name='Status')
    creationDt = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
    publicationDt = models.DateTimeField(auto_now=True, verbose_name='Data de publicação')
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name='Autor')
    theme = models.CharField(max_length=7, choices=themes, blank=False, null=False, verbose_name='Tema')
    title_slug = models.SlugField(default='')

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

