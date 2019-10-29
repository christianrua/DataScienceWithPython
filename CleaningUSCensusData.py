"""
Cleaning US Census Data

You just got hired as a Data Analyst at the Census Bureau, which collects census data and creates interesting visualizations and 
insights from it.

The person who had your job before you left you all the data they had for the most recent census. It is in multiple csv files. 
They didn’t use pandas, they would just look through these csv files manually whenever they wanted to find something. Sometimes 
they would copy and paste certain numbers into Excel to make charts.

The thought of it makes you shiver. This is not scalable or repeatable.

Your boss wants you to make some scatterplots and histograms by the end of the day. Can you get this data into pandas and into 
reasonable shape so that you can make these histograms?

"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import codecademylib3_seaborn
import glob

df0=pd.read_csv('states0.csv')
print(df0.head(),'\n')
print(df0.dtypes,'\n')

files=glob.glob('states*.csv')
df_list=[]
for filename in files:
  data=pd.read_csv(filename)
  df_list.append(data)
us_census=pd.concat(df_list).reset_index()

print(us_census.columns,'\n')
print(us_census.dtypes,'\n')

us_census['Income']=us_census['Income'].replace('[\$,]', '', regex=True)
us_census['Income']=pd.to_numeric(us_census['Income'])

print(us_census.Income.head())
us_census['Men']=us_census['GenderPop'].str.split('_',expand=True)[0]
us_census['Women']=us_census['GenderPop'].str.split('_',expand=True)[1]
print(us_census.head())

us_census['Men']=us_census['Men'].replace('M', '', regex=True)
us_census['Women']=us_census['Women'].replace('F', '', regex=True)

us_census['Men']=pd.to_numeric(us_census['Men'])
us_census['Women']=pd.to_numeric(us_census['Women'])

print(us_census.head())

plt.scatter(us_census['Men'],us_census['Women'])
plt.show()

us_census=us_census.fillna(value={'Women':us_census['TotalPop']-us_census['Men']})

print(us_census['Women'].head(10))

print(us_census.duplicated())

plt.scatter(us_census['Men'],us_census['Women'])
plt.show()

reaces=['Hispanic','White','Black','Native','Asian','Pacific']

for race in reaces:
  us_census[race]=us_census[race].replace('%', '', regex=True)
  us_census[race]=pd.to_numeric(us_census[race])
  plt.close('all')  
  plt.hist(us_census[race])
  plt.show()

plt.close('all')  
plt.hist(us_census['Hispanic'])
plt.show()
