#Makes the relevant imports
from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms import StringField, IntegerField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from application.models import Users, Conferences, Attendees
from flask_login import current_user

#All the forms and validators
class LoginForm(FlaskForm):
        username = StringField('Username',
                validators=[
                        DataRequired(),
                ]
        )

        password = PasswordField('Password',
                validators=[
                        DataRequired()
                ]
        )

        remember = BooleanField('Remember Me')
        submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
        first_name = StringField('First Name',
                validators=[
                        DataRequired(),
                        Length(min=2,max=30)
                ]
        )
        last_name = StringField('Last Name',
                validators=[
                        DataRequired(),
                        Length(min=1,max=30)
                ]
        )

        username = StringField('Username',
                validators=[
                        DataRequired(),
                        Length(min=2,max=30)
                ]
        )

        email = StringField('Email',
                validators=[
                        DataRequired(),
                        Email()
                ]
        )

        password = PasswordField('Password',
                validators=[
                        DataRequired(),
                ]
        )

        confirm_password = PasswordField('Confirm Password',
                validators=[
                        DataRequired(),
                        EqualTo('password')
                ]
        )
        submit = SubmitField('Sign Up')

        def validate_email(self, email):
                user = Users.query.filter_by(email=email.data).first()

                if user:
                        raise ValidationError('Email is already in use!')

class UpdateAccountForm(FlaskForm):
        first_name = StringField('First Name',
                validators=[
                        DataRequired(),
                        Length(min=2, max=30)
                ]
        )
        last_name = StringField('Last Name',
                validators=[
                        DataRequired(),
                        Length(min=2, max=30)
                ]
        )
        username = StringField('Username',
                validators=[
                        DataRequired(),
                        Length(min=2, max=30)
                ]
        )
        email = StringField('Email',
                validators=[
                        DataRequired(),
                        Email()
                ]
        )
        submit = SubmitField('Update')

        def validate_email(self, email):
                if email.data != current_user.email:
                        user = Users.query.filter_by(email=email.data).first()
                        if user:
                                raise ValidationError('Email already in use - Please choose another')


        
class ConferenceForm(FlaskForm):
        conference = StringField('Conference',
                validators=[
                        DataRequired(),
                        Length(min=2, max=60)
                ]
        )

        abstract = StringField('Abstract',
                validators=[
                        DataRequired(),
                        Length(min=2, max=2500)
                ]
        )

        speaker = StringField('Speaker',
                validators=[
                        DataRequired(),
                        Length(min=2, max=250)
                ]
        )

        company = StringField('Company',
                validators=[
                        DataRequired(),
                        Length(min=2, max=100)
                ]
        )

        email = StringField('Email',
                validators=[
                        DataRequired(),
                        Length(min=2, max=250)
                ]
        )

        bio = StringField('Biography',
                validators=[
                        DataRequired(),
                        Length(min=2, max=250)
                ]
        )

        submit = SubmitField('Add or Edit Conference')

class AttendeeForm(FlaskForm):
        conference = QuerySelectField(
                query_factory=lambda: Conferences.query.all(),
                get_label="conference"
        )

        name = StringField('Name',
                validators=[
                        DataRequired(),
                        Length(min=2, max=60)
                ]
        )

        company = StringField('Company',
                validators=[
                        DataRequired(),
                        Length(min=2, max=100)
                ]
        )

        email = StringField('Email',
                validators=[
                        DataRequired(),
                        Email()
                ]
        )

        submit = SubmitField('Add or Edit Attendee')
