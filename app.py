# Import the dependencies.
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List of all available api routes"""
    return (
        f"Available routes are as follows:<br/>"
        f"/api/v1.0/precipitation<br/>"
        "/api/v1.0/station<br/>"
        "/api/v1.0/tobs<br/>"
        "/api/v1.0/2010-01-01 and api/v1.0/2010-01-01/2010-12-31"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Establish session link
    session = Session(engine)
    
    # Query data and obtain precipitation data
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    prcp_data = session.query(measurement.date, measurement.prcp).\
    filter(measurement.date >= one_year_ago).all()
    
    session.close()
    
    #Convert precipitation data into dictionary using date as key
    #and prcp as the value
    prcp_dict ={}
    for date, prcp in prcp_data:
        prcp_dict[f"{date}"] = prcp
    
    # Return JSON representation of dictionary
    return(jsonify(prcp_dict))

@app.route("/api/v1.0/station")
def stations():
    # Establish session link
    session = Session(engine)
    
    # Query data and obtain station data
    station_data = session.query(station.station, station.name).all()
    
    session.close()
    
    # Create a dictionary from the row data and append to a list of stations
    station_list = []
    for s in station_data:
        station_dict = {}
        station_dict["station"] = s.station
        station_dict["name"] = s.name
        station_list.append(station_dict)
    
    # Return JSON list of stations
    return(jsonify(station_list))

@app.route("/api/v1.0/tobs")
def tobs():
    # Query data to rank stations by activity in descending order
    activity_list = session.query(station.station, func.count(measurement.id)).\
                    join(measurement, station.station == measurement.station).\
                    group_by(station.station).\
                    order_by(func.count(measurement.id).desc()).all()
                    
    most_active_station = activity_list[0][0]
    
    # Query the dates and temperature observations of the most-active station for the previous year of data.
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    tobs_data = session.query(measurement.date, measurement.tobs).\
    filter(measurement.station == most_active_station).\
    filter(measurement.date >= one_year_ago).all()
    
    session.close()
    
    # Create a dictionary from the row data and append to a list of temperature values
    temp_list = []
    for t in tobs_data:
        temp_dict = {}
        temp_dict["date"] = t.date
        temp_dict["temperature"] = t.tobs
        temp_list.append(temp_dict)
    
    # Return a JSON list of the temperature observations
    return(jsonify(temp_list))
    

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def your_start(start=None,end=None):
    # Establish session link
    session = Session(engine)
    
    query = [func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)]
 
    # If end date is provided, calculate statistics for the date range
    if end:
     temperature_data = session.query(*query).\
                         filter(measurement.date >= start).\
                         filter(measurement.date <= end).all()
    else:
     # If only start date is provided, calculate statistics from start date onwards
     temperature_data = session.query(*query).\
                         filter(measurement.date >= start).all()
 
    session.close()
 
    # Extract temperature statistics from the result
    (min_temp, avg_temp, max_temp) = temperature_data[0]
 
    # Create a dictionary to hold the temperature statistics
    temp_stats = {
     "start_date": start,
     "end_date": end,
     "min_temperature": min_temp,
     "avg_temperature": avg_temp,
     "max_temperature": max_temp
     }
 
    # Return the temperature statistics as JSON
    return jsonify(temp_stats)


if __name__ == '__main__':
    app.run(debug=True)























