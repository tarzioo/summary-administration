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
    firstname_of_decendent = db.Column(db.String(50), nullable=False)
    lastname_of_decedent = db.Column(db.String(50), nullable=False)
    case_number = db.Column(db.String(20), nullable=False)
    date_filed = db.Column(db.String(50), nullable=False)
    date_of_death = db.Column(db.String(50), nullable=False)
    court_date = db.Column(db.String(50), nullable=False)
    order_admitting_date = db.Column(db.String(50), nullable=True)


    @staticmethod
    def add_probate(firstname_of_decendent, lastname_of_decedent, case_number, date_filed, date_of_death, court_date, order_admitting_date):
        """Add a new probate"""


        probate = Probate(firstname_of_decendent=firstname_of_decendent, lastname_of_decedent=lastname_of_decedent, case_number=case_number, date_filed=date_filed, date_of_death=date_of_death, court_date=court_date, order_admitting_date=order_admitting_date)

        db.session.add(probate)
        db.session.commit()

        return probate

    @staticmethod
    def get_case_by_number(case_number):
        """Get existing case by case number"""


        probate = Probate.query.filter_by(case_number=case_number).first()

        return probate

    @staticmethod
    def update_order_admitting_date(case_number, order_admitting_date):
        """Update probate order admitting date"""


        probate = Probate.query.filter_by(case_number=case_number).first()
        probate.order_admitting_date = order_admitting_date
        db.session.commit()

        return probate


    def __repr__(self):
        """Provide helpful representation when printed"""


        return "<Probate probate_id=%s firstname_of_decendent=%s lastname_of_decedent=%s case_number=%s date_filed=%s date_of_death=%s court_date=%s order_admitting_date=%s>" % (self.probate_id, self.firstname_of_decendent, self.lastname_of_decedent, self.case_number, self.date_filed, self.date_of_death, self.court_date, self.order_admitting_date)









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