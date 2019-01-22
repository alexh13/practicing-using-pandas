# -pandas is a library used for data structures and data analysis tools.
# -used for loading data, web-scraping, loading & analyzing data from excel files
# * type ipython into to terminal *

import pandas

df1 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]])  # Create a dataframe named df1
print(df1)  # output dataFrame, numbers on left top - bottom are indexes, top left - right are columns
print()

# in pandas we can name columns individually using column= like this
df1 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]], columns=["Price", "Age", "Value"])
print(df1)
print()

# we can pass custom names for indexes as well using index=, like this
df1 = pandas.DataFrame([[2, 4, 6], [10, 20, 30]], columns=["Price", "Age", "Value"], index=["First", "Second"])
print(df1)
print()

# we can pass dictionaries too like this
df2 = pandas.DataFrame([{"Name": "Alex"}, {"Name": "Jack"}])
print(df2)
print()

# add a surname like this
df2 = pandas.DataFrame([{"Name": "Alex", "Surname": "Alexx"}, {"Name": "Jack"}])
print(df2)
print()

# we can get the mean like this
df1.mean()
print(df1.mean())
print()
# or the mean of the entire data frame like this
df1.mean().mean()
print(df1.mean().mean())
