from flask import request, jsonify
from models import Theatre, Movie
from database import db
from flask_restful import Resource
import traceback
from controllers.auth_controller import authorize 


class InsertTheatre(Resource):
    def get(self, t_name=None):
        if t_name is None:
            theatres = Theatre.query.all()
            theatre_list = []
            for theatre in theatres:
                theatre_data = { 
                    'id': theatre.id,
                    'tname': theatre.tname,
                    'city': theatre.city,
                    'capacity': theatre.capacity,
                }
                theatre_list.append(theatre_data)
            return jsonify(theatre_list)
        else:
            theatre = Theatre.query.filter_by(tname=t_name).first()
            if theatre:
                theatre_data = {
                    'id': theatre.id,                        
                    'tname': theatre.tname,
                    'city': theatre.city,
                    'capacity': theatre.capacity,
                }
                return jsonify(theatre_data)
            else:
                return jsonify({'message': 'Theatre not found'})
            
    
    def post(self):
        try:
            data = request.json
           
            new_theatre = Theatre(
                tname=data['tname'],
                city=data['city'],
                capacity=data['capacity']
            )

            db.session.add(new_theatre)
            db.session.commit()
                
            return jsonify({"message": "Successfully Inserted Theatre"}) 
        
        except Exception as e:
            return jsonify({"error": str(e)})
        
    
    def put(self,t_name):
        try:
            data = request.json
            
            theatres = Theatre.query.filter_by(tname=t_name).all()
            
            if theatres:

                new_tname = data.get('tname')
                
                
                if new_tname:  
                    
                    for theatre in theatres:
                        theatre.tname = new_tname
                    
                    movies = Movie.query.filter_by(theatre_name=t_name).all()
                    for movie in movies:
                        movie.theatre_name = new_tname

                    db.session.commit()
                    return jsonify({"message": "Successfully Updated Theatre"})
                else:
                    return jsonify({"message": "Theatre name not provided in the request"})
            else:
                return jsonify({"message": "Theatre Not found"})

        except Exception as e:
            return jsonify({"error":str(e)})
        
    
    def delete(self, t_name):
        try:
            print("t_name:",t_name)
            theatre = Theatre.query.filter_by(tname=t_name).first()
            print("movie:", theatre)
            print("theatre.id:", theatre.id)
            
            if theatre:
                Movie.query.filter_by(theatre_id=theatre.id).delete()
                print("theatre.id:", theatre.id)
                db.session.delete(theatre)
                db.session.commit()
                return jsonify({"message": "Theatre deleted successfully"})
            else:
                return jsonify({"message": "Theatre not found"})

        except Exception as e:
            traceback_info = traceback.format_exc()
            return jsonify({"error": str(e), "traceback": traceback_info})