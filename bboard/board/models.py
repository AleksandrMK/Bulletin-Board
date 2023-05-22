from django.db import models
from django.contrib.auth.models import User


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
    text = models.FileField(upload_to='uploads/')


class Response(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    article = models.ForeignKey(Ad, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
