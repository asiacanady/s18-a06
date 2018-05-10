'''
#3. Create a plot where the x-axis is the hour of the day and the y-axis is the
proportion of crimes occuring that hour that are domestic. Save this as
`prop_domestic_by_hour.png`.

Hint: You can extract the hour of a Timestamp using the `hour` attribute
(similar to `month` and `dayofweek` shown in lecture). Then `groupby` the hour
and aggregate the `Domestic` column.) We use the mean function
'''
import pandas as pd
df_crimes = pd.read_csv('crimes.csv')
import numpy as np
import matplotlib.pyplot as plt

df_crimes['Date'] = pd.to_datetime(df_crimes.Date)
hours = df_crimes.Date.dt.hour
series_crime = df_crimes['Domestic'].groupby(hours).mean()
reset = series_crime.reset_index()
reset.columns = ['Hours', 'Proportion of Crime']
#domestic = df_crimes[df_crimes['Domestic'] == True]
#domestic_count= domestic.Date.dt.hour.value_counts()
#df_crimes.Date.dt.hour.value_counts().plot(figsize=(12,8))
x = reset['Hours']
y = reset['Proportion of Crime']
plt.xlabel('Hours in The Day')
plt.ylabel('Proportion of Crimes that are Domestic')
plt.scatter(x, y)
plt.show()
plt.savefig('prop_domestic_by_hour.png')
