"""
Variance in Weather

You’re planning a trip to London and want to get a sense of the best time of the year to visit. Luckily, you got your hands on a 
dataset from 2015 that contains over 39,000 data points about weather conditions in London. Surely, with this much information, 
you can discover something useful about when to make your trip!

In this project, the data is stored in a Pandas DataFrame. If you’ve never used a DataFrame before, we’ll walk you through how to 
filter and manipulate this data. If you want to learn more about Pandas, check out our Data Science Path.

"""
import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data

print(london_data.iloc[100:200])
print(len(london_data))

temp=london_data["TemperatureC"]
average_temp=np.mean(temp)
temperature_var=np.var(temp)
temperature_standard_deviation=np.std(temp)

london_data.head()

june = london_data.loc[london_data["month"] == 6]["TemperatureC"]

july = london_data.loc[london_data["month"] == 7]["TemperatureC"]

print(np.mean(june))
print(np.mean(july))

print(np.std(june))
print(np.std(july))

for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["TemperatureC"]
  print("The mean temperature in month "+str(i) +" is "+ str(np.mean(month)))
  print("The standard deviation of temperature in month "+str(i) +" is "+ str(np.std(month)) +"\n")
