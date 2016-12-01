"""Models and database functions for project"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import joinedload
import datetime

# This is the connection to the PostgreSQL database; we're getting this through
# the Flask-SQLAlchemy helper library. On this, we can find the `session`
# object, where we do most of our interactions (like committing, etc.)

db = SQLAlchemy()


######################################################
# Model Definitions


class Probate(db.Model):
    """Details of probate being filed"""


    __tablename__ = "probate"

    probate_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    case_number = db.Column(db.String(20), nullable=False)
    date_filed = db.Column(db.String(50), nullable=False)


    @staticmethod
    def add_probate(firstname, lastname, case_number, date_filed):
        """Add a new probate"""


        probate = Probate(firstname=firstname, lastname=lastname, case_number=case_number, date_filed=date_filed)

        db.session.add(probate)
        db.session.commit()

        return probate






def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///probate'
    # app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."