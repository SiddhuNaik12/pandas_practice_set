import pandas as pd
#read data
df=pd.read_csv("set3_data.csv")
#concert date to datetime
df["date"]=pd.to_datetime(df["date"])
#filter data to single city
city_df=df[df["city"]=="Delhi"].sort_values("date")
#rolling 3 day average temperature
city_df["temp_3day_avg"]=city_df["temperature"].rolling(window=3).mean()
#detect humidity increase
city_df["humidity_increased"] = city_df["humidity"].diff()>0
print(city_df)