from rest_framework import serializers
from .models import Movies
from django.conf import  settings


class MovieSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = Movies
        fields = ['name', 'image', 'movie_link', 'movie_type', ]

    def get_image(self, obj):
        return '{}/{}'.format(settings.MEDIA_URL, obj.image)