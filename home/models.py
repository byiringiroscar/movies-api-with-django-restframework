from django.db import models


# Create your models here.

class Movies(models.Model):
    category = [
        ('action', 'action'),
        ('blockbuster', 'blockbuster'),
        ('horror', 'horror'),
        ('comedian', 'comedian'),
        ('thriller', 'thriller'),
        ('romance', 'romance'),

    ]
    name = models.CharField(max_length=100)
    image = models.ImageField()
    movie_link = models.URLField()
    movie_type = models.CharField(max_length=200, choices=category, default='action')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Movies'

    def __str__(self):
        return f'{self.name}'
