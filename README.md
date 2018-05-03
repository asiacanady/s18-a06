# Assignment 6: Further Exploration of Chicago Crimes
In this assignment we will continue to explore the Chicago crimes dataset using the more advanced operations we've learned including merging and group aggregation. Put the code for each question in files named `q1.py,...,q5.py`. Do not commit the CSV files to your git repository.

1. Load the crime data and parse the Date column. Also load the [community area socioeconomic data](https://data.cityofchicago.org/Health-Human-Services/Census-Data-Selected-socioeconomic-indicators-in-C/kn9c-c2s2) and get rid of the row corresponding to Chicago that is missing a `Community Area Number`.

    Calculate the number of crimes per community area. Merge this with the socioeconomic data to plot a scatter with per capita income on the x axis and crime count on the y axis. Save the plot as `crimes_by_income.png`.

  Hint:
   - Turn the crime counts into a dataframe using `reset_index()` as discussed lecture. Either name the community area nunber column `Community Area Number` to match the corresponding column in the socioeconomic data, or use separate `left_on` and `right_on` argument to `merge()`.
    - To make a scatter plot, call `plot()` on the DataFrame with an argument `kind='scatter'` and additional arguments `x` and `y` specifying the names of the columns to use for `x` and `y` data.
    
2. Repeat #1 for homicide counts and save the plot as `homocides_by_income.png`.

    Hint: The default, inner, merge between homocide counts and socioeconomic data will only include rows that had homocides. To get the right answer, you will need to select a different merge type using the `how` argument and then fill in the missing homocide counts with zeros.
  
3. Plot the proportion of crimes that are domestic by hour of the day. Save this as `prop_domestic_by_hour.png`.

    Hint: You can extract the hour of a Timestamp using the `hour` attribute (similar to `month` and `dayofweek` shown in lecture). Then groupby the hour and aggregate the `Domestic` column.

4. Chicago is divded into 77 [Community Areas](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Community-Areas-current-/cauq-8yn6/data), which were originally designated by sociologists at the University of Chicago in the 1920s. They are large neighborhoods. The Census Bureau, however, uses its own geographic partition to aggregate data, including population. These are called [census blocks](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Census-Blocks-2010/mfzt-js4n/data), which are grouped into [census tracts](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Census-Tracts-2010/5jrd-6zik/data).

    Download the [census block population data](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Population-by-2010-Census-Block/5yjb-v3mj), which contains the population of each census block. Also download the [census *tract* to community area mapping](tract_community.csv), which tells us which Community Area each tract belongs to. (Note that some census tracts cross a Community Area boundary but this file ignores that.)

    Merge these datasets on census tract to calculate the population of each community area. Put the result in a dataframe with two columns: Community Area and Population. Write the result to a CSV file called `community_populations.csv` using the `Data.Frame.to_csv()` function. (You may want to pass `index=False` so that it doesn't write the index column to the csv.)
    
    Hint: 
    - To merge the datasets you need to find the census tract for each block in the population data. By definition this is the first 6 digits of the block number. 
    - However, the data portal has a bug where if the leading digit was a zero it did not record it. Thus you need to convert the census blocks to strings of length 10 and then pad them using the `.str.zfill()` function.
    - The census tracts in the `tract_community.csv` mapping are full GeoIDs. The first few numbers represent Cook County. You'll need to ignore these and take only the last 6 digits by converting them to strings and indexing.
    - Finally you can merge the two datasets and group by Community area and aggregate the populations.

5. Merge the dataset you created in 5 with a count of homicides by community area to calculate the homicide rate per 100,000 capita in each community area. Merge this with the socioeconomic data, which contains the name of each community area, to find the community area with the highest crime *rate*. Include the name of this community area and its homicide rate in a comment at the end of `q5.py`.

6. Load the [police stations data](https://data.cityofchicago.org/Public-Safety/Police-Stations/z8bn-74gv). Join the crime data with the stations on police district. For each crime calculate the distance to the police station in miles. Then plot a histogram of the distances.

    Hint:
     - The station `DISTRICT` is a text field (because one of them is 'Headquarters') so you'll need to convert the crime `Distrct` to the same.
     - To calculate the distance use the included coordinates. (called `X Coordinates` and `Y Cooridnates` in the crime file; `X COORDINATES`, `Y COORDINATES` in the stations file). Find their distance in feet by taking the Euclidean distance (sqrt of dx squared plus dy squared) and then divide by 5280 to convert to miles.
     - By default the histogram will have 10 bins. You can increase that using the `bins` argument to `hist()`.
