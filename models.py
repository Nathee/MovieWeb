import datetime
import mongoengine


class MovieModel(mongoengine.Document):
    name = mongoengine.StringField(required=True, min_length=2, max_length=100)
    year = mongoengine.IntField(default=datetime.datetime.today().year, min_value=1900,
                                max_value=datetime.datetime.today().year + 5)
    genre = mongoengine.StringField(default='Unknown', min_length=3, max_length=20)
    rating = mongoengine.FloatField(default=0.0, min_value=0.0, max_value=10.0)
    actors = mongoengine.ListField(mongoengine.DictField(default={}))
    meta = {
        'db_alias': 'core',
        'collection': 'movies',
        'indexes': [
            'name',
            'year',
            'genre',
            'rating',
            'actors'
        ],
        'ordering': ['name']
    }
