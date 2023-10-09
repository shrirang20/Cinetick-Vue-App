from flask import request, jsonify
from models import Movie, Theatre
from database import db
from flask_restful import Resource
import traceback
from sqlalchemy import or_


class Search(Resource):
    def get(self):
        try:
            query = request.args.get('query', '')  # Get the 'query' parameter from the URL
            movies = Movie.query.filter(
                or_(
                    Movie.mname.contains(query),
                    Movie.theatre_name.contains(query),
                    Movie.date.contains(query),
                    Movie.start_time.contains(query),
                    Movie.end_time.contains(query),
                    Movie.language.contains(query),
                    Movie.tags.contains(query),
                    Movie.ticket_price.contains(query),
                )
            ).all()
            movie_data = [{
                'id': movie.id, 
                'mname': movie.mname, 
                'theatre_name': movie.theatre_name,
                'date': movie.date,
                'start_time': movie.start_time,
                'end_time': movie.end_time,
                'ticket_price': movie.ticket_price,
                'language': movie.language,
                'tags': movie.tags
                } for movie in movies]
            
            return {'movies': movie_data}, 200
        except Exception as e:
            traceback_info = traceback.format_exc()
            return jsonify({"error": str(e), "traceback": traceback_info}), 500


# class Search(Resource):
#     def get(self):
#         parser = reqparse.RequestParser()
#         parser.add_argument('query', type=str, required=True, help='Search query string')
#         args = parser.parse_args()
        
#         query = args['query']

#         print("PARSER:",parser)
#         print("ARGS:",args)
        
#         # Perform a database query to search for movies by name containing the query
#         movies = Movie.query.filter(Movie.mname.contains(query)).all()

#         # You can customize the data you want to send back to the frontend
#         movie_data = [{'id': movie.id, 'mname': movie.mname} for movie in movies]

#         return {'movies': movie_data}