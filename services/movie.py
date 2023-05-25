import init_django_orm  # noqa: F401
from typing import List, Optional
from django.db.models import QuerySet
from db.models import Movie


def get_movies(genres_ids: Optional[List[int]] = None,
               actors_ids: Optional[List[int]] = None) -> QuerySet:
    queryset = Movie.objects.all()
    if genres_ids and actors_ids:
        queryset = queryset.filter(genres__id__in=genres_ids, actors__id__in=actors_ids)
    elif genres_ids is not None:
        queryset = queryset.filter(genres__id__in=genres_ids)
    elif actors_ids is not None:
        queryset = queryset.filter(actors__id__in=actors_ids)
    return queryset


def get_movie_by_id(movie_id: int) -> QuerySet:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: Optional[List[int]] = None,
                 actors_ids: Optional[List[int]] = None) -> None:
    movie = Movie.objects.create(
        title=movie_title,
        description=movie_description)
    if genres_ids:
        movie.genres.set(genres_ids)
    if actors_ids:
        movie.actors.set(actors_ids)
