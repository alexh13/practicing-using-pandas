import pandas

df1 = pandas.read_json("supermarkets.json")  # read json file
print(df1)

# use drop to delete columns or rows
df1.drop("City", 1)
print(df1)

# updates df1 with the dropped data
df1 = df1.drop("City", 1)

# drop specific index
df1.drop(df1.index[0:3], 0)

# drop columns
df1.drop(df1.columns[0:3], 1)

