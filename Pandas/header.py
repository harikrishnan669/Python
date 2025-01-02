headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)

df.columns = headers
df.columns

df.head(10) # To show the first n names of the header
df.tail(10) # To show the last n names of the header

df1=df.replace('?',np.NaN)
df=df1.dropna(subset=["price"], axis=0)
df.head(20)

# The main datatypes in panadas are object,float,int,bool,datetime64
#To show the datatypes
df.dtypes
#to describe the datatypes
df.describe
