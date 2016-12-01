import json

from sqlalchemy import func
from model import Location
from model import User

from model import connect_to_db, db
from server import app







if __name__ == "__main__":
# As a convenience, if we run this module interactively, it will leave
# you in a state of being able to work with the database directly.

    connect_to_db(app)
    print "Connected to DB."

    #create location table
    db.create_all()

    load_location_data()