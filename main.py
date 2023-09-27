from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired
import json
from datetime import datetime


app = Flask(__name__)

with open('config.json', 'r') as config_file:
    config = json.load(config_file)['params']

app.config['SECRET_KEY'] = 'your_secret_key'

if config["local_server"] == "True":
    app.config['SQLALCHEMY_DATABASE_URI'] = config["local_uri"]
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = config["prod_uri"]

csrf = CSRFProtect(app)
db = SQLAlchemy(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = config["gmail-user"]
app.config['MAIL_PASSWORD'] = config["gmail-password"]
mail = Mail(app)

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])


class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)


class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, email):
        self.email = email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/contact')
def contact():
    form = ContactForm()
    return render_template('contact.html', form=form)



@app.route('/contact_submit', methods=['POST'])
def contact_submit():
    form = ContactForm(request.form)

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        message_text = form.message.data

        # Create a new ContactMessage object and add it to the database
        contact_message = ContactMessage(name=name, email=email, message=message_text)
        db.session.add(contact_message)
        db.session.commit()

        # Send an email notification
        msg = Message('New Contact Form Submission', sender=app.config['MAIL_USERNAME'], recipients=[app.config['MAIL_USERNAME']])
        msg.body = f'Name: {name}\nEmail: {email}\nMessage: {message_text}'
        mail.send(msg)

        # Send a thank-you message to the user
        thank_you_msg = Message('Thank You for Contacting Us', sender=app.config['MAIL_USERNAME'], recipients=[email])
        thank_you_msg.body = 'Thank you for contacting us. We will get back to you soon!'
        mail.send(thank_you_msg)

        flash('Message sent! We\'re glad to hear from you.', 'success')
        return redirect(url_for('contact'))

    flash('Form validation failed. Please check your input.', 'error')
    return redirect(url_for('contact'))

@app.route('/about')
def about():
    return render_template('about.html')


app.run(debug=True, host='127.0.0.1', port=5000)

