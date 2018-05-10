'''
#4. Merge these datasets on census tract to calculate the population of each
community area. Put the result in a dataframe with two columns: `Community Area`
and `Population`. Write the result to a CSV file called
`community_populations.csv` using the `DataFrame.to_csv()` function.
(You may want to pass `index=False` so that it doesn't write the index column
to the file.)

Hint:
- To merge the datasets you need to find the census tract for each block in the
population data. By definition this is the first 6 digits of the block number.

- However, the data portal has a bug where it dropped the leading digit if it
was a zero. Thus you need to convert the census blocks to strings, and then pad
them to length 10 with a leading zero using the `.str.zfill()` function.

- The census tracts in the `tract_community.csv` mapping are full GeoIDs. The
first few numbers represent Cook County. To match he tract in the popultaion
data you can ignore these digits and take only the last 6 digits by converting
them to strings and indexing.
-For example, you will want to pair `Census Tract` 17031031000 in
tract_community.csv with `CENSUS BLOCK` 310003002 in
`Population_by_2010_Census_Block.csv`.
- Finally you can merge the two datasets and group by Community area and
aggregate the populations.
'''
import pandas as pd
import numpy as  np
block_populations = pd.read_csv('Population_by_2010_Census_Block.csv')
tract_community = pd.read_csv('tract_community.csv')


block_populations['CENSUS BLOCK'] = block_populations['CENSUS BLOCK'].astype(str).str.zfill(10).str[0:6]
tract_community['Census Tract'] = tract_community['Census Tract'].astype(str).str[-6:]



block_populations.columns = ['Census Tract', 'Total Population']


merged_census = block_populations.merge(tract_community, on = 'Census Tract')
groupby_census = merged_census.groupby(['Community Area']).sum()
aggregate_final = groupby_census.reset_index()
aggregate_final.columns = ['Community Area', 'Total Population']


aggregate_final.to_csv('community_populations.csv', index = False)
