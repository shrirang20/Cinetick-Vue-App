from flask import Flask,request, jsonify
from database import db
from flask_restful import Api, Resource
from flask_cors import CORS
from controllers.auth_controller import Signup, Login
from controllers.crud_controller import InsertTheatre
from controllers.crud_movies import InsertMovie
from controllers.booking_controller import BookTicket
from controllers.search_controller import Search
from celery_worker import make_celery
import csv
from models import Movie, Theatre, Ticket, Admin
from sqlalchemy.orm import joinedload
from sqlalchemy import func
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from flask import Flask, jsonify, request


app = Flask(__name__)
app.secret_key = "AppDev2Project"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
db.init_app(app)

api =  Api(app)

CORS(app, resources={r'/*': {'origins': '*'}})

#Celery Codes
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)
celery = make_celery(app)

@celery.task(bind=True)
def export_theatre_data(self, theatre_id):
    try:
        # Retrieve theater details from the database
        theatre = Theatre.query.get(theatre_id)
        print("THEATRE-Celery:", theatre)

        # Replace 'num_shows', 'bookings', and 'rating' with actual computations
        theatre_name = theatre.tname
        movie_count = len(theatre.movies)

        # Calculate the total bookings for the theater
        total_bookings = 0
        for movie in theatre.movies:
            ticket_sum = db.session.query(func.sum(Ticket.num_tickets)).filter_by(movie_id=movie.id).scalar()
            if ticket_sum is not None:
                total_bookings += ticket_sum
            else:
                total_bookings += 0


        # Create a CSV file
        csv_filename = f'theatre_{theatre_id}_details.csv'
        csv_file_path = os.path.join(app.root_path, 'csv_exports', csv_filename)
        with open(csv_file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)

            # Write the CSV header row
            csv_writer.writerow(['Theatre Name', 'Movie Count', 'Total Bookings'])

            # Write the data row
            csv_writer.writerow([theatre_name, movie_count, total_bookings])

        csv_url = f'http://127.0.0.1:5000//csv_exports/theatre_{theatre_id}_details.csv'
        return csv_url
       
    except Exception as e:
        # Handle any exceptions and log them
        self.retry(exc=e)

class ExportTheatreCSV(Resource):
    def post(self, theatre_id):
        # Trigger the Celery task to export theater data
        task = export_theatre_data.apply_async(args=[theatre_id])

        task_result = task.get()
        print("TASK:",task)
        # Send a response to the admin indicating that the job has been triggered
        return jsonify({"message": "Export job has been triggered.", "task_id": task.id, "file_url": task_result})

api.add_resource(ExportTheatreCSV, '/export-theatre-csv/<int:theatre_id>')

#MONTHTLY REPORT 


def get_monthly_data():
    current_month = datetime.now().month
    current_year = datetime.now().year

    movie_count = db.session.query(func.count(Movie.id)).filter(
        db.extract('month', Movie.date) == current_month,
        db.extract('year', Movie.date) == current_year
    ).scalar()

    total_bookings = db.session.query(func.sum(Ticket.num_tickets)).filter(
        db.extract('month', Movie.date) == current_month,
        db.extract('year', Movie.date) == current_year
    ).scalar()

    return {
        'bookings': total_bookings,
        'shows_seen': movie_count,
    }

SMTP_SERVER_HOST = "localhost"
SMTP_SERVER_PORT = 1025
SENDER_EMAIL = "21f1002870@ds.study.iitm.ac.in"
SENDER_PASSWORD = ""  # For SMTP, this can be left empty

def send_mail(to, subject, message_body):
    msg = MIMEMultipart()
    msg["To"] = to
    msg["From"] = SENDER_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(message_body, "html"))

    server = smtplib.SMTP(host=SMTP_SERVER_HOST, port=SMTP_SERVER_PORT)
    server.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
    server.send_message(msg)
    server.quit()

def generate_and_send_report():
    # Replace this part with your report generation code
    report_data = "<h1>Monthly Report</h1><p>This is the monthly report content.</p>"

    # Modify the email subject and recipient as needed
    email_subject = "Monthly Report"
    recipient_email = "shrirang.sapate95@gmail.com"

    # Send the report as an email
    send_mail(recipient_email, email_subject, report_data)



api.add_resource(Signup, '/auth/signup')
api.add_resource(Login, '/auth/login')
api.add_resource(InsertTheatre, '/auth/insert','/auth/insert/<int:t_id>','/auth/insert/<string:t_name>')
api.add_resource(InsertMovie, '/auth/insert/movies','/auth/insert/movies/<int:theatreId>')
api.add_resource(BookTicket, '/auth/book-ticket','/auth/book-ticket/<int:movie_id>')
api.add_resource(Search, '/auth/search-movies')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
    generate_and_send_report()

