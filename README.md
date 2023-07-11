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

