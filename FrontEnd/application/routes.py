from flask import abort, render_template, redirect, url_for, request, flash
from application.forms import RegistrationForm, LoginForm, UpdateAccountForm, CountryForm
from application.models import Users
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

#Render the about page
@app.route('/accountgenerator', methods=['GET', 'POST'])
@login_required
def accountgenerator():
	
	#list User's name
	user = Users.query.get(current_user.id)

	form = CountryForm()
	if form.validate_on_submit():
		country = form.country.data
		try:
			iban = requests.post('http://central-service:5000/post-iban', json={"Country":country})
			if iban.ok:
				current_user.iban = iban.json()["IBAN"]
				current_user.accountnumber = iban.json()["BankAccount"]
				current_user.sortcode = iban.json()["Sort"]
				current_user.cardnumber = iban.json()["CardNumber"]
				current_user.cvc = iban.json()["CVC"]
				db.session.commit()
				flash('You have successfully generated a bank account!')
				return redirect(url_for('accountgenerator'))
		except:
			flash('Error')
		return redirect(url_for('accountgenerator'))

	return render_template('accountgenerator.html', title='Account Generator', user=user, form=form)

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

@app.route('/new-iban', methods=['GET', 'POST'])
def iban():
	iban = requests.post('http://central-service:5000/post-iban', json={"Country":"Pakistan"})
	if iban.ok:
		current_user.iban = iban.json()["IBAN"]
		current_user.accountnumber = iban.json()["BankAccount"]
		current_user.sortcode = iban.json()["Sort"]
		current_user.cardnumber = iban.json()["CardNumber"]
		current_user.cvc = iban.json()["CVC"]
		db.session.commit()
		return redirect(url_for('accountgenerator'))
	return "OK\n"
