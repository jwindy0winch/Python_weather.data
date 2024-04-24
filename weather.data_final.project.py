import pandas as pd
OG_data = pd.read_csv("/Users/winch/OneDrive/Davenport.edu/Python Programming/Final Weather data project/HistoricalData.csv")

#Filters Columns
filtered_data = OG_data[['STATION', 'NAME', 'DATE', 'AWND', 'SNOW']].copy()
#Saves filtered data
filtered_data.to_csv("filteredData.csv", index=False)

#DATE to datetime conversion
filtered_data['DATE'] = pd.to_datetime(filtered_data['DATE'])

#Extract Year & Month
filtered_data['YEAR'] = filtered_data['DATE'].dt.year
filtered_data['MONTH'] = filtered_data['DATE'].dt.month

#Calculate Average Snow per month for location & year
average_snow = filtered_data.groupby(['YEAR', 'NAME', 'MONTH'], as_index=False)['SNOW'].mean()
#Calculate Total Snow per month for each location & year
total_snow = filtered_data.groupby(['YEAR', 'NAME', 'MONTH'], as_index=False)['SNOW'].sum()

#Average Snow, Split Data by Year
average_snow_2016 = average_snow[average_snow['YEAR'] == 2016]
average_snow_2017 = average_snow[average_snow['YEAR'] == 2017]
#Total Snow, Split Data by Year
total_snow_2016 = total_snow[total_snow['YEAR'] == 2016]
total_snow_2017 = total_snow[total_snow['YEAR'] == 2017]
#Saving Average Snow data for 2016/2017
average_snow_2016.to_csv("average2016.csv", index=False)
average_snow_2017.to_csv("average2017.csv", index=False)
#Saving Total Snow data for 2016/2017
total_snow_2016.to_csv("total2016.csv", index=False)
total_snow_2017.to_csv("total2017.csv", index=False)

#Sort Average Snow data for 2016/2017
sorted_average_snow_2016 = average_snow_2016.sort_values(by='SNOW', ascending=False).head(3)
sorted_average_snow_2017 = average_snow_2017.sort_values(by='SNOW', ascending=False).head(3)

#Top 3 Locations
top3_data = pd.concat([sorted_average_snow_2016, sorted_average_snow_2017], axis=1)
#Saving Top 3 Locations
top3_data.to_csv("top3.csv", index=False)

#Top 10 AWND Readings
top10_AWND = filtered_data.nlargest(10, 'AWND')
#Saving Top 10 AWND Readings
top10_AWND.to_csv("top10AWND.csv", index=False)