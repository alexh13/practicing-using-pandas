# use a jupyter notebook for this, or call ipython in terminal

import pandas

# --------how to load csv files in pandas------------- #
df1 = pandas.read_csv("supermarkets.csv")
print(df1)
# setting id as my index
df1.set_index("ID")
# get shape of my data frame
print(df1.shape)

# --------how to load json files in pandas------------- #
df2 = pandas.read_json("supermarkets.json")
df2.set_index("ID")
print(df2)

# --------how to load excel files in pandas------------- #
# normally pass another parameter for excel files, pass the sheet number
df3 = pandas.read_excel("supermarkets.xlsx", sheet_name=0)
print(df3)

# --------how to load text files in pandas------------- #
df4 = pandas.read_csv("supermarkets_commas.txt")
print(df4)

# --------how to load other values as separators files in pandas------------- #
df5 = pandas.read_csv("supermarkets-semi-colons.txt", sep=";")
print(df5)

# --------how to load online files from the web in pandas------------- #
df6 = pandas.read_csv("insert weblink here/filename.csv")
# json file:
df7 = pandas.read_json("insert weblink here/filename.json")

