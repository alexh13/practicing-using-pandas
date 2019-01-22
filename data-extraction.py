# use jupyter notebook or ipython in terminal

import pandas

df1 = pandas.read_json("supermarkets.json")  # read json file
print(df1)

# get in the habit of applying new variables when changing existing data frames
df2 = df1.set_index("Address")  # set index to the address, change that variable
print(df2)

# to slice a portion of data we use loc like this
# .loc for label based indexing
df3 = df2.loc["735 Dolores St":"332 Hill St", "Country":"ID"]
print(df3)

# can convert data to a list like this
print(list(df2.loc[:, "Country"]))

# common way to extract data from data frame using iloc
# .iloc for positional indexing
df4 = df2.iloc[1:3, 1:3]  # the range of indexes i want
print(df4)

