from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


class Ad(models.Model):
    TYPE = (
        ('tank', 'Танки'),
        ('healer', 'Хилы'),
        ('dd', 'ДД'),
        ('vendors', 'Торговцы'),
        ('gm', 'Гилдмастеры'),
        ('quest', 'Квестгиверы'),
        ('smith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('potion', 'Зельевары'),
        ('spellmaster', 'Мастера заклинаний'),
    )
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    category = models.CharField(max_length=16, choices=TYPE, default='tank')
    text = RichTextField()
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title.title()}'

    def get_absolute_url(self):
        return reverse('ad', args=[str(self.id)])


class Response(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    article = models.ForeignKey(Ad, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('ad', args=[str(self.Ad.id)])

    # def __str__(self):
    #     return self.author.title()
