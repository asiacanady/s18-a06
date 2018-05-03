# Assignment 6: Further Exploration of Chicago Crimes
In this assignment we will continue to explore the Chicago crimes dataset using the more advanced operations we've learned including merging and group aggregation. Put the code for each question in files named `q1.py,...,q5.py`.

1. Load the crime data and parse the Date column. Also load the [community area socioeconomic data](https://data.cityofchicago.org/Health-Human-Services/Census-Data-Selected-socioeconomic-indicators-in-C/kn9c-c2s2) and get rid of the row corresponding to Chicago that is missing a `Community Area Number`.

Calculate the number of crimes per community area. Merge this with the socioeconomic data to plot a scatter with per capita income on the x axis and crime count on the y axis. Save the plot as `crimes_by_income.png`.

  Hint:
   - Turn the crime counts into a dataframe. Either name the community area nunber column `Community Area Number` to match the corresponding column in the socioeconomic data, or use separate `left_on` and `right_on` argument to `merge()`.
    - To make a scatter plot, call `plot()` on the DataFrame with an argument `kind='scatter'` and additional arguments `x` and `y` specifying the names of the columns to use for `x` and `y` data.
    
2. Repeat #1 for homicide counts and save the plot as `homocides_by_income.png`.

  Hint: The default, inner, merge between homocide counts and socioeconomic data will only include rows that had homocides. To get the right answer, you will need to select a different merge type using the `how` argument and then fill in the missing homocide counts with zeros.
  
3. Plot the proportion of crimes that are domestic by hour of the day. Save this as `prop_domestic_by_hour.png`.

  Hint: You can extract the hour of a Timestamp using the `hour` attribute (similar to `month` and `dayofweek` shown in lecture). Then groupby the hour and aggregate the `Domestic` column.
  
4. Use `groupby` and `agg` to create a single table with each primary crime type's arrest arrest rate and count. Then reanswer question 3 from assignment 5.

5. Chicago is divded into 77 [Community Areas](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Community-Areas-current-/cauq-8yn6/data), which were originally designated by sociologists at the University of Chicago in the 1920s. They are large neighborhoods. The Census Bureau, however, uses its own geographic partition to aggregate data, including population. These are called [census blocks](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Census-Blocks-2010/mfzt-js4n/data), which are grouped into [census tracts](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Census-Tracts-2010/5jrd-6zik/data).

Download the [census block population data](https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Population-by-2010-Census-Block/5yjb-v3mj), which contains the population of each census block. Also download the census *tract* to community area mapping, which tells us which Community Area each tract belongs to. (Note that some census tracts cross a Community Area boundary but we'll ignore that for now).

Use these datasets to calculate the population of each community area.
