from flask import Flask, render_template, jsonify, make_response, abort, request
from flasgger import Swagger, swag_from
from schema_validation import validate_rating
import movies_dao

app = Flask(__name__)
host_name = '127.0.0.1'
app.config['SWAGGER'] = {
    'title': 'Movies REST API',
    'uiversion': 3,
    'version': '1.1'
}
swagger = Swagger(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/movies', methods=['GET'])
@swag_from('docstrings/get_movies.yml')
def get_movies():
    return jsonify(movies_dao.get_all_movies())


@app.route('/movies/<string:movie_name>', methods=['GET'])
@swag_from('docstrings/get_movie.yml')
def get_movie(movie_name):
    res = movies_dao.get_movie(movie_name)
    if res is None:
        abort(404)
    return jsonify(res)


@app.route('/movies/rating/<float:rating>', methods=['GET'])
@swag_from('docstrings/get_rating_movie.yml')
def get_movies_gte_rating(rating):
    if rating < 0 or rating > 10:
        abort(400)
    res = movies_dao.get_movies_gte_rating(rating)
    if not res:
        abort(404)
    return jsonify(res)


@app.route('/actor/<string:name>', methods=['GET'])
@swag_from('docstrings/get_actor.yml')
def get_actors_movies(name):
    res = movies_dao.get_actors_movies(name)
    if not res:
        abort(404)
    return jsonify(res)


@app.route('/count/movies', methods=['GET'])
@swag_from('docstrings/get_counted_movies.yml')
def get_counted_movies():
    return jsonify({'moviesCount': movies_dao.count_movies()})


@app.route('/movies', methods=['POST'])
@swag_from('docstrings/post_movie.yml')
def post_movie():
    if not request.json or 'movieName' not in request.json:
        abort(400)
    movie_name = request.json['movieName']
    if 'movieData' not in request.json:
        movies_dao.save_movie({'name': movie_name})
    else:
        movie_data = request.json['movieData']
        movies_dao.save_movie_with_data({'name': movie_name, 'year': movie_data.get('year'),
                                         'genre': movie_data.get('genre'), 'rating': movie_data.get('rating'),
                                         'actors': movie_data.get('actors')})
    return jsonify({'Added movie': movie_name}), 201


@app.route('/movies/<string:movie_name>/rating', methods=['PUT'])
@swag_from('docstrings/put_movie.yml')
def update_review(movie_name):
    req_name = 'rating'
    if not request.json or req_name not in request.json:
        abort(400)
    # if rating < 0 or rating > 10:
    #     abort(400)
    if not validate_rating([request.json]):
        abort(400)
    rating = request.json[req_name]
    if not movies_dao.update_rating(movie_name, rating):
        abort(404)
    return jsonify({'Updated review of movie': movie_name}), 201


@app.route('/movies/<string:movie_name>/remove', methods=['DELETE'])
@swag_from('docstrings/del_movie.yml')
def delete_movie(movie_name):
    if not movies_dao.delete_movie(movie_name):
        abort(404)
    return jsonify({'Removed movie': movie_name})


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(500)
def internal_server(error):
    return make_response(jsonify({'error': 'Internal server error'}), 500)


if __name__ == '__main__':
    app.run(host=host_name)
