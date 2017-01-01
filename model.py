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

class User(db.Model):
    """Details of lawfirm's login for probate app"""


    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    
    @staticmethod
    def add_user(username, password):
        """Add new user"""


        user = User(username=username, password=password)

        db.session.add(user)
        db.session.commit()
        return user


    def __repr__(self):
        """Provide helpful representation when printed"""


        return "<User user_id=%s username=%s >" % (self.user_id, self.username)






class Probate(db.Model):
    """Details of probate being filed"""


    __tablename__ = "probates"

    probate_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fullname_of_decendent = db.Column(db.String(75), nullable=False)
    case_number = db.Column(db.String(20), nullable=False)
    date_filed = db.Column(db.String(50), nullable=True)
    date_of_death = db.Column(db.String(50), nullable=False)
    court_date = db.Column(db.String(50), nullable=True)
    order_admitting_date = db.Column(db.String(50), nullable=True)


    # timeline = db.relationship("Timeline", backref=db.backref("probate"))



    @staticmethod
    def add_probate(fullname_of_decendent, case_number, date_filed, date_of_death, court_date, order_admitting_date):
        """Add a new probate"""


        probate = Probate(fullname_of_decendent=fullname_of_decendent, case_number=case_number, date_filed=date_filed, date_of_death=date_of_death, court_date=court_date, order_admitting_date=order_admitting_date)

        db.session.add(probate)
        db.session.commit()

        return probate

    @staticmethod
    def get_case_by_number(case_number):
        """Get existing case by case number"""


        print "entered get case by number function"
        probate = Probate.query.filter_by(case_number=case_number).first()
        print "probate in model file is", probate

        return probate

    @staticmethod
    def get_by_probate_id(probate_id):
        """get existing probate by probate id"""


        probate = Probate.query.filter_by(probate_id=probate_id).first()


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


        return "<Probate probate_id=%s fullname_of_decendent=%s case_number=%s date_filed=%s date_of_death=%s court_date=%s order_admitting_date=%s>" % (self.probate_id, self.fullname_of_decendent, self.case_number, self.date_filed, self.date_of_death, self.court_date, self.order_admitting_date)



# class Timeline(db.Model):
#     """Details of lawfirm's login for probate app"""


#     __tablename__ = "timelines"

#     timeline_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     order_admitting_date = db.Column(db.String(50), db.ForeignKey('probates.order_admitting_date'))
#     first_10_days = db.Column(db.String(50), nullable=True)
#     second_10_days = db.Column(db.String(50), nullable=True)
#     thirty_days = db.Column(db.String(50), nullable=True)

#     probate = db.relationship("Probate", backref=db.backref("timelines"))

#     def __repr__(self):
#         """Provide helpful representation when printed"""


#         return "<User timeline_id=%s first_10_days=%s second_10_days=%s  thirty_days=%s>" % (self.user_id, self.first_10_days, self.second_10_days, self.thirty_days)






def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///summary_administration'
    # app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."