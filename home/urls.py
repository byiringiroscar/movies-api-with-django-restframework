from django.urls import  path
from .views import *


urlpatterns = [
    path('movie/<id>/', get_movie, name="get-movie")
]