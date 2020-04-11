from application import db
from datetime import datetime
from flask_login import UserMixin
from datetime import datetime
from wtforms.ext.sqlalchemy.fields import QuerySelectField

#Create the Users table
class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    
    def __repr__(self):
            return ''.join(['User ID: ', str(self.id), '\r\n',  
                            'Email: ', self.email, '\r\n',
                           'Name: ', self.first_name, ' ', self.last_name])


class Attendees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    conference_id = db.Column(db.Integer, db.ForeignKey('conferences.id'), nullable=False)

    def __repr__(self):
        return  ''.join([
            'Attendee',  self.name, '\r\n',
            self.company
            ])

class Conferences(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    conference = db.Column(db.String(60), nullable=False, unique=True)
    abstract = db.Column(db.String(2500), nullable=False)
    speaker = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    bio = db.Column(db.String(250), nullable=False, unique=True)
    attendees = db.relationship('Attendees', backref='conference_ref', lazy=True)

    def __repr__(self):
        return ''.join([
            'Conference: ', self.conference, '\r\n',
            'Speaker: ', self.speaker
            ])
