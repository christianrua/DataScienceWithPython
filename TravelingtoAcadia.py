"""
Traveling to Acadia

Imagine you work at a travel agency and want to inform your customers of the best time to visit one of your favorite vacation 
locations, Acadia, Maine. In this project, you will use flower bloom data, and flight information to recommend the best time of 
year for someone to make a trip to Maine.

In script.py, we’ve imported the following data:

    in_bloom is a NumPy array containing 900 numbers. Each number is a day of the year, which represents the average start date of 
    a flower blooming.
    flights is a NumPy array with 11,000 numbers. Each number is a day of the year, which represents a flight from your hometown 
    to airports near Acadia, Maine.

Your goal is to create two histograms, each displaying the frequency of an occurrence each day of the year (either flights or 
flower blooms).

You will use the in_bloom variable to find a count of the number of flowers that start blooming each day of the year.

You will use the flights variable to find a count of the number of flights that occur each day of the year.

"""

# import codecademylib3
import codecademylib3
import numpy as np
from matplotlib import pyplot as plt

# load in data
in_bloom = np.loadtxt(open("in-bloom.csv"), delimiter=",")
flights = np.loadtxt(open("flights.csv"), delimiter=",")

# Plot the histograms
plt.figure(1)
plt.subplot(211)
plt.hist(flights,range=(0,365),bins=365)
plt.xlabel('day of the year')
plt.ylabel('numbers of flights')

plt.subplot(212)
plt.hist(in_bloom, range=(0, 365), bins=365)
plt.title("Flower Blooms and Flights by Day")
plt.ylabel("Bloom Count")
plt.xlabel("Day of the Year")
plt.show()
