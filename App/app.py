from collections.abc import Mapping, Sequence
from typing import Any
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError


app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'R#DFR45yf665$6cffe#r67*#*&455423FDGTFTDR$'
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False , unique=True)
    password = db.Column(db.String(80))

class registrationForm(FlaskForm): #registration form class
    username = StringField(validators=[InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})
    #username
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=80)], render_kw={"placeholder": "Password"})
    #password
    submit = SubmitField("Register")
    
    def validate(self, username):
        existing_user_username = User.query.filter_by(
           username=username.data 
        )

@app.route('/')
def home():
    return redirect(url_for('Welcome'))

@app.route('/Welcome')
def Welcome():
    return render_template("Welcome.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

if __name__ == '__main__':
    app.run(debug=True)
    
