from flask import request, jsonify
from models import Movie, Theatre, Ticket
from database import db
from flask_restful import Resource

class BookTicket(Resource):
    def post(self, movie_id):
        data = request.get_json()
        print("DATA:",data)
        user_id = data.get('user_id')
        #movie_id = data.get('movie_id')
        num_tickets = data.get('num_tickets')

        # Check if the movie exists
        movie = Movie.query.get(movie_id)
        print("MOVIE BCAKEND:",movie)
        if movie:
            # Check if the theater has enough capacity
            if int(num_tickets) <= int(movie.theatre.capacity):
                # Update the theater's remaining capacity
                movie.theatre.capacity -= num_tickets

                # Create ticket records
                
                ticket = Ticket(user_id=user_id, movie_id=movie.id, num_tickets=num_tickets)
                db.session.add(ticket)
                db.session.commit()

                return jsonify({"message": "Tickets booked successfully."})
            else:
                return jsonify({"message": "Not enough capacity for booking tickets."})
        else:
            return jsonify({"message": "Movie not found."})



# class BookTicket(Resource):
#     def post(self):
#         data = request.get_json()
#         user_id = data.get('user_id')
#         movie_id = data.get('movie_id')
#         num_tickets = data.get('num_tickets')

#         # Check if the theater has enough capacity
#         movie = Movie.query.get(movie_id)
#         if movie:
#             theatre = Theatre.query.get(movie.theatre_id)
#             if theatre:
#                 remaining_capacity = theatre.capacity - theatre.ticketsBooked
#                 if num_tickets <= remaining_capacity:
#                     # Update the ticketsBooked count for the movie
#                     movie.ticketsBooked += num_tickets
#                     db.session.commit()

#                     # Create ticket records
#                     for _ in range(num_tickets):
#                         ticket = Ticket(user_id=user_id, movie_id=movie_id, num_tickets=1)
#                         db.session.add(ticket)
#                     db.session.commit()

#                     return jsonify({"message": "Tickets booked successfully."})
#                 else:
#                     return jsonify({"message": "Not enough capacity for booking tickets."})
#             else:
#                 return jsonify({"message": "Theatre not found."})
#         else:
#             return jsonify({"message": "Movie not found."})
