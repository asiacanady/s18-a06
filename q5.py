'''
Merge the dataset you created in #4 with a count of homicides by community area
to calculate the homicide rate per 100,000 capita in each community area. Merge
this with the socioeconomic data, which contains the name of each community
area, to find the community area with the highest homicide *rate*. Include the
name of this community area and its homicide rate in a comment at the end of
`q5.py`.
'''

import pandas as pd
tract_community = pd.read_csv('census.csv')
df_crimes = pd.read_csv('crimes.csv')
block_populations = pd.read_csv('community_populations.csv')

homicides = df_crimes[df_crimes['Primary Type'] == 'HOMICIDE']
homicidesdf = homicides.groupby('Community Area').size().reset_index(name = 'Number of Homicides')
homicides_crimes = block_populations.merge(homicidesdf, on = 'Community Area', how = 'inner')
homicides_crimes['Rate per 100000']=(homicides_crimes['Number of Homicides'] / homicides_crimes['Total Population'])*100000


tract_community.rename(columns={'Community Area Number':'Community Area'}, inplace=True)
community_homicides = homicides_crimes.merge(tract_community, on = 'Community Area', how = 'inner')

community_homicides = community_homicides.sort_values(by = 'Rate per 100000')

print(community_homicides.tail(1)['COMMUNITY AREA NAME'], community_homicides.tail(1)['Rate per 100000'])

#North Lawndale has the highest rate of homicides at approx. 119 per 100,000 people.





#the community with the most homicides is
