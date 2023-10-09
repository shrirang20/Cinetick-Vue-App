from flask import request, jsonify
from models import Movie, Theatre
from database import db
from flask_restful import Resource  
import traceback
from controllers.auth_controller import authorize 

class InsertMovie(Resource):
    def get(self, theatreId=None):
        if theatreId is None:
            movies = Movie.query.all()
            movie_list = []
          
            for movie in movies: 
                movie_data = { 
                    'id': movie.id,
                    'mname': movie.mname,
                    'theatre_name': movie.theatre_name,
                    'city': movie.city,
                    'date': movie.date,
                    'start_time': movie.start_time,
                    'end_time': movie.end_time,
                    'ticket_price': movie.ticket_price,
                    'language': movie.language,
                    'tags': movie.tags,
                    'theatre_capacity': movie.theatre.capacity
                }
                movie_list.append(movie_data)
            return jsonify(movie_list)
        else:
            movie = Movie.query.filter_by(id=theatreId).first()
            if movie:
                movie_data = { 
                    'id': movie.id,                        
                    'mname': movie.mname,
                    'theatre_name': movie.theatre_name,
                    'city': movie.city,
                    'date': movie.date,
                    'start_time': movie.start_time,
                    'end_time': movie.end_time,
                    'ticket_price': movie.ticket_price,
                    'language': movie.language,
                    'tags': movie.tags,
                    'theatre_capacity': movie.theatre.capacity
                }
                return jsonify(movie_data)
            else:
                return jsonify({'message': 'Movie not found'})

   
    def post(self):
        try:
            data = request.json
            
            theatre_name = data['theatre_name']
            city = data['city']
            
            theatre = Theatre.query.filter_by(tname=theatre_name, city=city).first()
            
            if theatre is None:
                
                return jsonify({"error": f"Theatre '{theatre_name}' in '{city}' does not exist. Please create the theatre first."})
            
            
            new_movie = Movie(
                mname=data['mname'],
                theatre_name=data['theatre_name'],
                city=data['city'],
                date=data['date'],
                start_time=data['start_time'],
                end_time=data['end_time'],
                ticket_price=data['ticket_price'],
                language=data['language'],
                tags=data['tags'],
                theatre_id=theatre.id
            )
            
            db.session.add(new_movie)
            db.session.commit()
              
            return jsonify({"message": "Successfully Inserted Movie"})
        
        except Exception as e:
            return jsonify({"error": str(e)})

   
    def put(self,theatreId):
        try:
            data = request.json

            movie = Movie.query.filter_by(id=theatreId).first()

            if movie:

                new_theatre_name = data.get('theatre_name', movie.theatre_name)
                new_city = data.get('city', movie.city)

                theatre = Theatre.query.filter_by(tname=new_theatre_name, city=new_city).first()

                if theatre:
                    movie.mname = data['mname']
                    movie.theatre_name = data['theatre_name']
                    movie.city = data['city']
                    movie.date = data['date']
                    movie.start_time = data['start_time']
                    movie.end_time = data['end_time']
                    movie.ticket_price = data['ticket_price']
                    movie.language = data['language']
                    movie.tags = data['tags']
                    movie.theatre_id = theatre.id

                    db.session.commit()
                    return jsonify({"message":"Updation Sucessful"})
                else:
                    return jsonify({"message":"Updation Failed! Theatre not found"})
            else:
                return jsonify({"message":"Updation Failed! Movie not found"})

        except Exception as e:
            traceback_info = traceback.format_exc()
            return jsonify({"error": str(e), "traceback": traceback_info})
        
   
    def delete(self, theatreId):
        try:
            print("theatreId:",theatreId)
            movie = Movie.query.filter_by(id=theatreId).first()
            print("movie:", movie)
            if movie:
                db.session.delete(movie)
                db.session.commit()
                return jsonify({"message": "Movie deleted successfully"})
            else:
                return jsonify({"message": "Movie not found"})

        except Exception as e:
            traceback_info = traceback.format_exc()
            return jsonify({"error": str(e), "traceback": traceback_info})
        
