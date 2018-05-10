'''
Load the [police stations data]
(https://data.cityofchicago.org/Public-Safety/Police-Stations/z8bn-74gv). Join
the crime data with the stations on police district. For each crime,
calculate the distance to the police station in miles. Then plot a histogram of
these distances and save it to `crimes_by_distance.png`.
'''
import pandas as pd
stations_df = pd.read_csv('Police_Stations.csv')

df_crimes = pd.read_csv('crimes.csv')
df_crimes['District'] = df_crimes['District'].astype(str).str[:-2]
crimes_districts = df_crimes.merge(stations_df, left_on='District', right_on = 'DISTRICT')

x_distance = crimes_districts['X COORDINATE'] - crimes_districts['X Coordinate']
y_distance = crimes_districts['Y COORDINATE'] - crimes_districts['Y Coordinate']

import numpy as np
x_distance**2 + y_distance**2
distance = np.sqrt(x_distance**2 + y_distance**2)
miles = distance / 5280

import matplotlib.pyplot as plt
miles.hist(bins = 12)
plt.xlabel('Distance to Police Station in Miles')
plt.ylabel('Frequency of Crimes')
plt.show()
plt.savefig('crimes_by_distance.png')
