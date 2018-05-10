'''
2. Repeat #1 for homicide counts and save the plot as `homocides_by_income.png`.
Hint: The homicide counts will be missing rows for community areas that had no
homicides. The default, inner, merge between homocide counts and socioeconomic
data will thus be missing these areas. To get the right answer, you will need to
select a different merge type using the `how` argument and then fill in the
missing homocide counts with zeros.
'''
import pandas as pd
df_crimes = pd.read_csv('crimes.csv')

df_community = pd.read_csv('census.csv')
df_community[:-1]
print(df_community)


homicides = df_crimes[df_crimes['Primary Type'] == 'HOMICIDE']
homicidesdf = homicides['Community Area'].value_counts()
print(homicidesdf)

homicides_count = homicidesdf.reset_index()
homicides_count.columns = ['Community Area Number', 'Homicides']
merged = homicides_count.merge(df_community, on = 'Community Area Number', how ='outer')

import numpy as np
import matplotlib.pyplot as plt


x = merged['PER CAPITA INCOME ']
y = merged['Homicides'].fillna(0)
plt.xlabel('Per Capita Income')
plt.ylabel('Homicides')
plt.scatter(x, y)
plt.show()
plt.savefig('homicides_by_income.png')
