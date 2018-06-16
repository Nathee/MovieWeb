from mongo_setup import init_db
from models import MovieModel
import json


def get_all_movies():
    init_db('movie-web')
    query = MovieModel.objects()
    res = json.loads(query.to_json())
    return res


def get_movie(movie_name):
    init_db('movie-web')
    query = MovieModel.objects(name=movie_name).first()
    if query is None:
        return None
    res = json.loads(query.to_json())
    return res


def get_movies_gte_rating(rating):
    init_db('movie-web')
    query = MovieModel.objects(rating__gte=rating)
    res = json.loads(query.to_json())
    return res


def get_actors_movies(actor_name):
    init_db('movie-web')
    query = MovieModel.objects(actors__actor=actor_name)
    res = json.loads(query.to_json())
    movies_w_actor = []
    for movie in res:
        role = 'Unknow'
        for actor in movie['actors']:
            if actor['actor'] == actor_name:
                role = actor['role']
        movies_w_actor.append({'movieName': movie['name'], 'role': role})
    return movies_w_actor


def save_movie(movie_json):
    init_db('movie-web')
    movies_schema = MovieModel()
    movies_schema.name = movie_json['name']
    movies_schema.save()


def save_movie_with_data(movie_json):
    init_db('movie-web')
    movies_schema = MovieModel()
    movies_schema.name = movie_json['name']
    movies_schema.year = movie_json['year']
    movies_schema.genre = movie_json['genre']
    movies_schema.rating = movie_json['rating']
    movies_schema.actors = movie_json['actors']
    movies_schema.save()


def update_rating(movie_name, rating):
    init_db('movie-web')
    movie = MovieModel.objects(name=movie_name).first()
    if movie is None:
        return False
    movie.update(set__rating=float(rating))
    return True


def delete_movie(movie_name):
    init_db('movie-web')
    movie = MovieModel.objects(name=movie_name).first()
    if movie is None:
        return False
    movie.delete()
    return True


def count_movies():
    init_db('movie-web')
    count = MovieModel.objects().count()
    return count
