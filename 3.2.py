"""
3.2 The type of vehicle the U.S public purchases varies depending on many factors. Table 1060
from the U.S. Census Bureau, Statistical Abstract of the United States: 2012 provides the following
data. The numbers reported are in thousands of units; that is, 9,300 represents 9,300,000 vehicles
sold in 1990.

a. Construct a graph that would display the changes from 1990 to 2010 in the public’s
choice in vehicle.
"""
import matplotlib.pyplot as pyplot
import numpy as np
year = []
passenger = []
suv = []
df = open('./ex3-2.txt', 'r')
for row in df:
    row = row.split(',')
    year.append(row[0])
    passenger.append(int(row[1]))
    suv.append(int(row[2]))

pyplot.bar(np.arange(len(passenger)) - 0.2, passenger, 0.4, label='Passenger')
pyplot.bar(np.arange(len(suv)) + 0.2, suv, 0.4, label='SUV')
pyplot.xticks(range(len(year)), year)
pyplot.legend(loc='upper right')
pyplot.show()

"""
b. Do you observe any trends in the type of vehicle purchased? What factors may be
influencing these trends?

I notice that before 2000, people bought a significantly higher amount of passenger
vehicles than SUVs. This could be because following the gas crisis that ended in 1980,
people were less interested in buying cars that used more gas (SUVs). However, after 2000,
people began buying more SUVs than passenger cars. This could be because the gas crisis was far
in the past, and people began to show interest in buying larger vehicles again. I also
notice that after 2008, people began purchasing less cars in general. This could be because
of the financial crisis of 2008, which affected many peoples' purchasing capabilities.
"""