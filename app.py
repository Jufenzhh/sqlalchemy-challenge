# Import the dependencies.

from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import datetime as dt
from sqlalchemy import MetaData
import numpy as np


#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
# reflect the tables
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

def welcome():
    return (
        f"Welcome to the Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date<br/>"
        f"/api/v1.0/start_date/end_date"
    )

@app.route('/api/v1.0/precipitation')
def precipitation():
    # Calculate the date one year ago from the last date in the database
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    last_date = dt.datetime.strptime(last_date[0], '%Y-%m-%d')
    one_year_ago = last_date - dt.timedelta(days=365)
# Query for the date and precipitation for the last 12 months
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= one_year_ago).all()

    # Convert the query results to a dictionary
    precipitation_data = {date: prcp for date, prcp in results}

    return jsonify(precipitation_data)

@app.route('/api/v1.0/stations')
def stations():
    # Query for the stations
    results = session.query(Station.station).all()

    # Convert the query results to a list
    station_list = list(np.ravel(results))

    return jsonify(station_list)

@app.route('/api/v1.0/tobs')
def tobs():
    # Calculate the date one year ago from the last date in the database
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    last_date = dt.datetime.strptime(last_date[0], '%Y-%m-%d')
    one_year_ago = last_date - dt.timedelta(days=365)

    # Query for the temperature observations for the last 12 months for the most active station
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= one_year_ago).\
        filter(Measurement.station == 'USC00519281').all()

    # Convert the query results to a list
    tobs_list = list(np.ravel(results))

    return jsonify(tobs_list)

@app.route('/api/v1.0/<start>')
@app.route('/api/v1.0/<start>/<end>')
def start_end(start=None, end=None):
    # Define the query for the summary statistics based on start and end dates
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        # Calculate the summary statistics for all dates greater than or equal to the start date
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        
        # Convert the query results to a list
        summary_stats = list(np.ravel(results))
    else:
        # Calculate the summary statistics for dates between the start and end dates
        results = session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()

        # Convert the query results to a list
        summary_stats = list(np.ravel(results))
    
    return jsonify(summary_stats)

if __name__ == '__main__':
    app.run(debug=True)