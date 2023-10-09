from database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(10), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(10), nullable=False)
    role_id = db.Column(db.Integer,nullable=False)


class Theatre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tname = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    movies = db.relationship('Movie', backref='theatre', lazy=True)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mname = db.Column(db.String(100), nullable=False)
    theatre_name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String, nullable=False)
    start_time = db.Column(db.String, nullable=False)
    end_time = db.Column(db.String, nullable=False)
    ticket_price = db.Column(db.Float, nullable=False)
    language = db.Column(db.String(50), nullable=False)
    tags = db.Column(db.String(100), nullable=False)
    theatre_id = db.Column(db.Integer, db.ForeignKey('theatre.id'), nullable=False)


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False)
    num_tickets = db.Column(db.Integer, nullable=False)



