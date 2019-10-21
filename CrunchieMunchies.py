"""
CrunchieMunchies

You work in marketing for a food company YummyCorps, which is developing a new kind of tasty, wholesome cereal called 
CrunchieMunchies. You want to demonstrate to consumers how healthy your cereal is in comparison to other leading brands, so you’ve 
dug up nutritional data on several different competitors.

Your task is to use NumPy statistical calculations to analyze this data and prove that your CrunchieMunchies cereal is the 
healthiest choice for consumers. 
"""

import codecademylib
import numpy as np

calorie_stats=np.genfromtxt('cereal.csv', delimiter=',')

average_calories=np.mean(calorie_stats)
print(average_calories)

calorie_stats_sorted=np.sort(calorie_stats)
print(calorie_stats_sorted)

median_calories=np.median(calorie_stats)
print(median_calories)

r5percentile=np.percentile(calorie_stats,5)
r10percentile=np.percentile(calorie_stats,10)
r25percentile=np.percentile(calorie_stats,25)
r50percentile=np.percentile(calorie_stats,50)
r75percentile=np.percentile(calorie_stats,75)

print(r5percentile)
print(r10percentile)
print(r25percentile)
print(r50percentile)
print(r75percentile)

nth_percentile=r5percentile

more_calories=np.mean(calorie_stats>60)
print(more_calories)

calorie_std=np.std(calorie_stats)
print(calorie_std)
