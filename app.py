import os

from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, connect_db, Pet

app = Flask(__name__)

app.config['SECRET_KEY'] = (os.environ.get('SECRET_KEY', 'noonewilleverknow'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = (os.environ.get('DATABASE_URL', 'postgresql:///heroku'))

connect_db(app)
db.create_all()

@app.route("/")
def home_page():
    """Show homepage"""
    return render_template('index.html')

@app.route("/pet", methods=["GET"])
def list_pets():
    pets = [pet.to_json() for pet in Pet.query.all()]
    return jsonify(pets), 200

@app.route("/pet", methods=["POST"])
def create_pet():
    new_pet = Pet(name="blaze")
    db.session.add(new_pet)
    db.session.commit()

    return '', 204
