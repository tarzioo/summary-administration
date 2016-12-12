from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from urllib2 import Request, urlopen, URLError
import requests
from pprint import pprint
import json

from model import *

app = Flask(__name__)

#required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """homepage"""

    return render_template("homepage.html")


@app.route("/add-probate", methods=["POST"])
def add_probate():
    """add new probate case"""


    fullname_of_decendent = request.form.get('fullname_of_decendent')
    case_number = request.form.get('case_number')
    date_filed = request.form.get('date_filed')
    date_of_death = request.get('date_of_death')
    court_date = request.form.get('court_date')
    order_admitting_date = request.form.get('order_admitting_date')

    Probate.add_probate(fullname_of_decendent, case_number,
        date_filed, date_of_death, court_date, order_admitting_date)


    return "Probate case added"
    

@app.route("/add-case")
def add_case():
    """add case"""


    return render_template('add-case.html')


@app.route("/probate-progress")
def probate_progress():
    """Show progress of probate"""

    return render_template("probate-progress.html")









if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    #app.debug = True

    connect_to_db(app)
    db.create_all()

    # Use the DebugToolbar
    #DebugToolbarExtension(app)

    app.run(host="0.0.0.0")