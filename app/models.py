from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_pokemon = db.relationship('UserPokemon', backref='Author', lazy=True)

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = generate_password_hash(password)

class UserPokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    ability = db.Column(db.String(30))
    base_experience = db.Column(db.Integer)
    sprite = db.Column (db.String)
    attack_base_stat = db.Column(db.Integer)
    hp_base_stat = db.Column(db.Integer)
    defense_base_stat = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, name, ability, base_experience, sprite, attack_base_stat, hp_base_stat, defense_base_stat, user_id):
        self.name = name
        self.ability = ability
        self.base_experience = base_experience
        self.sprite = sprite
        self.attack_base_stat = attack_base_stat
        self.hp_base_stat = hp_base_stat
        self.defense_base_stat = defense_base_stat
        self.user_id = user_id


