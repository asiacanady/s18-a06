'''
1. Load the 2017 crime data from assignment 5. Also load the [community area
socioeconomic data]
(https://data.cityofchicago.org/Health-Human-Services/Census-Data-Selected-socioeconomic-indicators-in-C/kn9c-c2s2)
and get rid of the row corresponding to the whole city of Chicago
(it's missing a `Community Area Number`).

'''
import pandas as pd
df_crimes = pd.read_csv('crimes.csv')

df_community = pd.read_csv('census.csv')
df_community[:-1]
print(df_community)
