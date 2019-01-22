# use a jupyter notebook for this, or call ipython in terminal

import pandas

df1 = pandas.read_json("supermarkets.json")  # read json file
print(df1)

# ---------- Add new column ------------------#

# have to pass a list with the exact number of items in our data frame/table. We have 5.
df1["Continent"] = df1.shape[0]*["North America"]  # new column name - Value
# using shape[0]* we multiply it by "North America" to fill in our data frame

# modifying column, updated continent column
df1["Continent"] = df1["Country"] + "," + "North America"


# ---------- Add new row ------------------#

# T is a method that transposes data frame
df1_t = df1.T
# check new data frame, rows become columns and columns become rows
print(df1_t)
# now we can use the same syntax to add a new column
df1_t["My Address"] = ["My City", "My Country", 10, 7, "My Shop", "My State", "My Continent"]
print(df1_t)

# switch back to correct rows and columns
df1 = df1_t.T
print(df1)



