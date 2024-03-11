Climate Analysis and Flask App

## Project Overview

This project includes an analysis of climate data for Honolulu, Hawaii, and the design of a Flask API based on the analysis. The project has been completed, and this README serves as documentation for the project.

Project Structure

The project consists of two main parts:

1. **Analysis and Exploration of Climate Data**:
   - Utilized Python and SQLAlchemy for basic climate analysis and data exploration.
   - Conducted precipitation and station analysis.
   - Visualized the data using Pandas and Matplotlib.
   - Analyzed the provided SQLite database (`hawaii.sqlite`) containing climate data.

2. **Design of Flask API**:
   - Implemented Flask routes for accessing the analyzed climate data.
   - Provided routes for retrieving precipitation data, station data, temperature observations, and temperature statistics.

### Part 1: Analysis and Exploration of Climate Data

In this section, Python and SQLAlchemy were used to analyze and explore the climate data. The following steps were completed:

- Connected to the SQLite database using SQLAlchemy.
- Reflected tables into classes using `automap_base()` and saved references to the classes named `station` and `measurement`.
- Linked Python to the database by creating a SQLAlchemy session.
- Performed precipitation analysis and station analysis as outlined in the provided instructions.

### Part 2: Climate App

The Flask API was designed based on the queries developed during the analysis phase. The following route designs were implemented:

- `/`: Started at the homepage and listed all available routes.
- `/api/v1.0/precipitation`: Converted the query results from precipitation analysis to a dictionary using date as the key and prcp as the value. Returned the JSON representation of the dictionary.
- `/api/v1.0/stations`: Returned a JSON list of stations from the dataset.
- `/api/v1.0/tobs`: Queried the dates and temperature observations of the most-active station for the previous year of data. Returned a JSON list of temperature observations for the previous year.
- `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`: Returned a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

## Repository Structure

- **climate_starter.ipynb**: Jupyter Notebook containing the climate data analysis.
- **app.py**: Flask application file containing the API routes.
- **hawaii.sqlite**: SQLite database containing the climate data.
- **README.md**: This README file providing an overview of the project.

## Tools Used

- Python
- SQLAlchemy
- Pandas
- Matplotlib
- Flask

## Conclusion

This project has provided valuable insights into the climate of Honolulu, Hawaii, and has successfully implemented a Flask API for accessing the analyzed data.
