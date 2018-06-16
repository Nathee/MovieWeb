import mongoengine
from data import movies
from models import MovieModel


def init_db(db_name: str):
    mongoengine.register_connection(alias='core', name=db_name)


def disconnect():
    mongoengine.connection.disconnect(alias='core')


def fill_movies_collection():
    for movie_json in movies:
        movies_schema = MovieModel()
        movies_schema.name = movie_json['name']
        movies_schema.year = movie_json['year']
        movies_schema.genre = movie_json['genre']
        movies_schema.rating = movie_json['rating']
        movies_schema.actors = movie_json['actors']
        movies_schema.save()


if __name__ == '__main__':
    init_db('movie-web')
    fill_movies_collection()
    print('Operation successful. Content added:')
    for movie in MovieModel.objects:
        print(movie.name)
