# geocoding is converting addresses to coordinates
# reverse geocoding is converting coordinates to addresses
# **use jupyter notebook or ipython in terminal**

import pandas
from geopy.geocoders import ArcGIS

# convert string to latitude longitude
non = ArcGIS()
non1 = non.geocode("3995 23rd St, San Francisco, CA 94114")  # put address here, geocode accepts this format
non1  # outputs: Location(3995 23rd St, San Francisco, California, 94114, (37.75298458728149, -122.4317017142651, 0.0))
print(non1.latitude)  # outputs lat
print(non1.longitude)  # outputs longitude

df = pandas.read_csv("supermarkets.csv")
df

# create a new column containing correct amount of data needed for geocode
df["Address"] = df["Address"] + ", " + df["City"] + ", " + df["State"] + ", " + df["Country"]

# create new column to store needed string to geocode
df["Coordinates"] = df["Address"].apply(non.geocode)  # apply used for what method to apply to the values of the address column
df  # call it

df.Coordinates  # to access entire text for location

df.Coordinates.latitude  # for latitude

