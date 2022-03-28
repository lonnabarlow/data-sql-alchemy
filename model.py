"""Models and database functions for cars db."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
# Here's where we create the idea of our database. We're getting this through
# the Flask-SQLAlchemy library. On db, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


##############################################################################
# Part 1: Compose ORM

class Human(db.Model):
    """Human model."""

    __tablename__ = "humans"
    human_id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(80), unique=True, nullable=False)
    lname = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    animals = relationship("Animal")

class Animal(db.Model):
    """Animal model."""

    __tablename__ = "animals"
    animal_id = db.Column(db.Integer, primary_key=True)
    human_id = db.Column(db.Integer)
    name = db.Column(db.String(80), unique=True, nullable=False)
    animal_species = db.Column(db.String(80), unique=True, nullable=False)
    birth_year = db.Column(db.Integer)

    human_id = db.Column(db.Integer, db.ForeignKey('humans.human_id'),
        nullable=False)
    human = relationship("Human", back_populates="animals")
    # human = db.relationship('Human',
    #     backref=db.backref('animals', lazy=True))



# End Part 1


##############################################################################
# Helper functions

def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app.
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print("Connected to DB.")


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our database.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tictbfqqthwbhg:416ca050a26bcc4bb4d97f29206abea727a0579ab964dd824b905f994a95e834@ec2-18-215-96-22.compute-1.amazonaws.com:5432/d33tvo52e8c6i6'
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    init_app()