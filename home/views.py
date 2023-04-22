from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Movies
from .serializers import MovieSerializer


# Create your views here.


@api_view(['GET', ])
def get_movie(request, id):
    try:
        movie = Movies.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
