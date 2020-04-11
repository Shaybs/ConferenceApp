from flask import abort, render_template, redirect, url_for, request, flash
from application.forms import RegistrationForm, LoginForm, UpdateAccountForm, AttendeeForm, ConferenceForm
from application.models import Users, Attendees, Conferences
from application import app, db, bcrypt, login_manager
import requests
from flask_login import login_user, current_user, logout_user, login_required

#Render the home page
@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html', title='Home')

#Render the about page
@app.route('/about')
def about():
	return render_template('about.html', title='About')



@app.route('/conferences', methods=['GET', 'POST'])
@login_required
def conferences():
    #List all conference
    conferences = Conferences.query.all()
    return render_template('conferences.html', title='Conferences', conferences=conferences)


@app.route('/conferences/add', methods=['GET', 'POST'])
@login_required
def add_conference():

    add_conference = True

    form = ConferenceForm()
    if form.validate_on_submit():
        conference = Conferences(
        conference=form.conference.data,
        abstract=form.abstract.data,
        speaker=form.speaker.data,
        company=form.company.data,
        email=form.email.data,
        bio=form.bio.data,
        )
        try:
            db.session.add(conference)
            db.session.commit()
            flash('You have successfully added a new book')
        except:
            flash('Error: The book already exists')
        return redirect(url_for('conferences'))

    return render_template('conference.html', action="Add", title='Add Conference', form=form, add_conference=add_conference)

@app.route('/conferences/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_conferences(id):

    add_conference = False

    conference = Conferences.query.get_or_404(id)
    form = ConferenceForm(obj=book)
    if form.validate_on_submit():
        conference.conference = form.conference.data
        conference.abstract = form.abstract.data
        conference.speaker = form.speaker.data
        conference.company = form.company.data
        conference.email = form.email.data
        conference.bio = form.bio.data
        db.session.commit()
        flash('You have successfully edited the conference')
        #return to conferences list
        return redirect(url_for('conferences'))


    form.conference.data = conference.conference
    form.abstract.data = conference.abstract
    form.speaker.data = conference.speaker
    form.company.data = conference.company
    form.email.data = conference.email
    form.bio.data = conference.bio

    return render_template('conference.html', action="Edit", add_conference=add_conference, conference=conference, form=form, title="Edit Conference")

@app.route('/conferences/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_conferences(id):

    attendees = Attendees.query.filter_by(conference_id=id)
    for attendee in attendees:
        db.session.delete(attendee)

    conference = Conferences.query.get_or_404(id)
    db.session.delete(conference)
    db.session.commit()
    flash('You have successfully deleted a conference')

    return redirect(url_for('conferences'))

    return render_template(title="Delete Conferences")


@app.route('/attendees')
@login_required
def attendees():

    attendees = Attendees.query.all()

    return render_template('attendees.html', title='Attendees', attendees=attendees)


    name = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


@app.route('/attendees/add', methods=['GET', 'POST'])
@login_required
def add_attendees():

    add_attendee = True

    form = AttendeeForm()
    if form.validate_on_submit():
        attendee = Attendees(
        name=form.name.data,
        company=form.company.data,
        email=form.email.data,
        conference_ref=form.conference.data
        )
        try:
            db.session.add(attendee)
            db.session.commit()
            flash('You have successfully added a new Attendee')
        except:
            flash('Error: The attendee already exists')
        return redirect(url_for('attendees'))

    return render_template('attendee.html', action="Add", title='Add Attendee', form=form, add_attendee=add_attendee)

@app.route('/attendees/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_attendee(id):

    add_attendee = False

    attendee = Attendees.query.get_or_404(id)
    form = ReviewForm(obj=review)
    if form.validate_on_submit():
        attendee.name = form.name.data
        attendee.company = form.company.data
        attendee.email = form.email.data
        conference_ref = form.conference.data
        db.session.commit()
        flash('You have successfully edited the Attendee')
        #return to attendees list
        return redirect(url_for('attendees'))

    form.conference.data = review.conference_ref
    form.name.data = attendee.name
    form.company.data = attendee.company
    form.email.data = attendee.email

    return render_template('attendee.html', action="Edit", add_attendee=add_attendee, attendee=attendee, form=form, title="Edit Attendee")

@app.route('/attendees/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_attendee(id):
    attendee = Attendees.query.get_or_404(id)
    db.session.delete(attendee)
    db.session.commit()
    flash('You have successfully deleted the attendee')
    return redirect(url_for('attendees'))

    return render_template(title="Delete Attendee")



#Render the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))

	form = LoginForm()
	if form.validate_on_submit():
		user=Users.query.filter_by(username=form.username.data).first()

		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember=form.remember.data)
			next_page = request.args.get('next')

			if next_page:
				return redirect(next_page)
			else:
				return redirect(url_for('home'))

	return render_template('login.html', title='Login', form=form)

@app.route('/logout')
@login_required
def logout():
        logout_user()
        return redirect(url_for('login'))

#Render the Registration
@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))

	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_pw = bcrypt.generate_password_hash(form.password.data).decode('utf-8')

		user = Users(
			first_name=form.first_name.data,
			last_name=form.last_name.data,
			username=form.username.data,
			email=form.email.data,
			password=hashed_pw
		)

		db.session.add(user)
		db.session.commit()
		flash('You have successfully registered! You can now login')
		return redirect(url_for('login'))

	return render_template('register.html', title='Register', form=form)

@login_manager.user_loader
def load_user(id):
	return Users.query.get(int(id))

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
	form = UpdateAccountForm()

	if form.validate_on_submit():
		current_user.first_name = form.first_name.data
		current_user.last_name = form.last_name.data
		current_user.username = form.username.data
		current_user.email = form.email.data
		db.session.commit()
		flash('You have successfully updated your details!')
		return redirect(url_for('account'))
	elif request.method == 'GET':
		form.first_name.data = current_user.first_name
		form.last_name.data = current_user.last_name
		form.username.data = current_user.username

	return render_template('account.html', title='Account', form=form)

