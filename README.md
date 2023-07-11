# sqlalchemy-challenge
The first script in climate_starter.ipynb performs climate analysis on weather data from the Hawaii database. It retrieves precipitation data, station information, and temperature statistics.
It does this by first importing the necessary libraries and their dependencies: pandas, matplotlib, SQLAlchemy, datetime 
Then it creates an engine object that connects to the "hawaii.sqlite" database using SQLAlchemy.
The script reflects the existing database into a new model using automap_base() and prepare() functions. This allows accessing the tables in the database as classes.
The code then  queries the database to retrieve the last 12 months of precipitation data. It creates a Pandas DataFrame with the results and plots the data using Matplotlib.
A summary statistic table is created for the value of precipitation using the pandas dataframe 
The script calculates the total number of stations in the dataset by querying the "station" table
It finds the most active stations by counting the number of observations for each station and orders them in descending order, for the most active station, the script calculates the lowest, highest, and average temperature by querying the "measurement" table
It queries the last 12 months of temperature observation data for the most active station and plots the results as a histogram
Finally, the script closes the session.

The second script in app.py begins by importing the necessary dependencies for building a Flask application and working with a database
It sets up the database connection by creating an engine object using SQLAlchemy and specifying the path to the SQLite database file ("sqlite:///Resources/hawaii.sqlite")
The script reflects the existing database into a new model using automap_base() and prepare() functions. This allows accessing the tables in the database as classes
It saves references to the "measurement" and "station" tables by mapping them to classes
The script creates a Flask application instance
It defines routes and corresponding functions for the Flask application.
The /api/v1.0/precipitation route queries the database for the last year's precipitation data and returns it as JSON.
The /api/v1.0/stations route queries the database for the list of stations and returns it as JSON.
The /api/v1.0/tobs route queries the database for the temperature observations for the last year from a specific station and returns them as JSON.
The /api/v1.0/<start> and /api/v1.0/<start>/<end> routes calculate summary statistics (minimum, average, and maximum temperatures) based on a start date and an optional end date and return them as JSON.
The code includes a special block if __name__ == '__main__': to ensure that the Flask application is run only when the script is executed directly.
Finally, the application is run with the app.run() function, and the Flask application is started in debug mode.
