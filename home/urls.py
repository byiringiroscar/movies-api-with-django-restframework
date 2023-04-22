from django.urls import  path
from .views import *


urlpatterns = [
    path('movie/', get_all_movies, name="get-all-movie"),
    path('movie/<id>/', get_movie, name="get-movie"),
    path('movie/<id>/', update_movie, name="update-movie"),
    path('movie/<id>/', delete_movie, name="delete-movie"),
]