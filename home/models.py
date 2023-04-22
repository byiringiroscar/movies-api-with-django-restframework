from django.db import models


# Create your models here.

class Movies(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    movie_link = models.URLField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Movies'

    def __str__(self):
        return f'{self.name}'
