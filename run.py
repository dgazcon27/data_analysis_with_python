# Import pandas library
import pandas as pd

# Read the online file by the URL provides above, and assign it to variable "df"
other_path = "automobile.csv"
df = pd.read_csv(other_path, header=None)

# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df.columns = headers
# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe\n") 
df.head(5)
#Saving dataset
# df.to_csv("automobile.csv", index=False)
# Show the last 10 rows
# df.tail(10) 