from jinja2 import StrictUndefined

from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from urllib2 import Request, urlopen, URLError
import requests
from pprint import pprint
import json
from datetime import datetime
from pytz import timezone

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

@app.route('/login')
def login():
    """Login Page"""

    return render_template("login.html")


@app.route("/add-probate", methods=["POST"])
def add_probate():
    """add new probate case"""


    fullname_of_decendent = request.form.get('fullname_of_decendent')
    case_number = request.form.get('case_number')
    date_filed = request.form.get('date_filed')
    date_of_death = request.form.get('date_of_death')
    court_date = request.form.get('court_date')
    order_admitting_date = request.form.get('order_admitting_date')

    Probate.add_probate(fullname_of_decendent, case_number,
        date_filed, date_of_death, court_date, order_admitting_date)

    result = Probate.get_case_by_number(case_number)


    return redirect('/probate-progress')
    

@app.route("/add-case")
def add_case():
    """add case"""


    return render_template('add-case.html')


@app.route("/case-search", methods=["POST"])
def search_for_a_case():
    """Search for a case by case number"""


    print "**************************"
    print "entered case search route"
    case_number = request.form.get("case_number")
    print "received from search field", case_number

    probate = Probate.get_case_by_number(case_number)
    print "Case Number is", case_number


    #Since date_filed, court_date, and order_admitting date can be set as null, we use '- - -' as a place filler until it is given a date

    if not probate.date_filed:
        probate.date_filed = "- - -"
    if not probate.court_date:
        probate.court_date = "- - -"
    if not probate.order_admitting_date:
        probate.order_admitting_date = "- - -"

    probate_json = {
                    'Probate_id': probate.probate_id,
                    'fullname_of_decendent': probate.fullname_of_decendent,
                    'case_number': probate.case_number,
                    'date_filed': probate.date_filed,
                    'date_of_death': probate.date_of_death,
                    'court_date': probate.court_date,
                    'order_admitting_date': probate.order_admitting_date
    }

    pprint(probate_json)

    probate_id = str(probate.probate_id)

    return redirect('/probate-progress/' + probate_id)

@app.route("/probate-progress/<probate_id>")
def probate_progress(probate_id):
    """Show progress of probate"""

    probate = Probate.get_by_probate_id(int(probate_id))

    if not probate.date_filed:
        probate.date_filed = "- - -"
    if not probate.court_date:
        probate.court_date = "- - -"
    if not probate.order_admitting_date:
        probate.order_admitting_date = "- - -"

    print "recevied get by probate", probate

    return render_template("probate-progress.html", probate=probate)

@app.route('/schedule-planner')
def schedule_planner():
    """Show current day to help plan possible court dates 30 and 45 days out"""

    

    # time = datetime.datetime.now()

    fmt = "%Y-%m-%d %H:%M:%S %Z%z"

    # Current time in UTC
    now_utc = datetime.now(timezone('UTC'))
    print now_utc.strftime(fmt)

    # Convert to US/central time zone
    now_central = now_utc.astimezone(timezone('US/Central'))
    print now_central.strftime(fmt)


    return render_template("schedule-planner.html", now_central=now_central)








if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    #app.debug = True

    connect_to_db(app)
    db.create_all()

    # Use the DebugToolbar
    #DebugToolbarExtension(app)

    app.run(host="0.0.0.0")