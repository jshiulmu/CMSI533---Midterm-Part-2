"""
3.10 The following table presents homeownership rates, in percentages, by state for the years
1985, 1996, and 2002. These values represent the proportion of homes owned by the occupant to
the total number of occupied homes. (rented vs. owned)

a. Construct relative frequency histogram plots for the homeownership data given in
the table for the years 1985, 1996, and 2002.
b. What major differences exist among the plots for the three years?
c. Why do you think the plots have changed over these 17 years?
d. How could Congress use the information in these plots for writing tax laws that
allow major tax deductions for homeownership?
"""

import matplotlib.pyplot as pyplot
import numpy as np

#a
df = open('./ex3-10.txt', 'r')
eighty_five = []
ninety_six = []
o_two = []
for row in df:
    row = row.split(',')
    eighty_five.append(float(row[1]))
    ninety_six.append(float(row[2]))
    o_two.append(float(row[3]))
fig, (a, b, c) = pyplot.subplots(nrows=1, ncols=3)
bins = 25
a.hist(eighty_five, np.linspace(min(eighty_five) - 3, max(eighty_five), bins), weights=np.ones_like(eighty_five)/len(eighty_five))
a.set_title("1985 relative frequency")

b.hist(ninety_six, np.linspace(min(ninety_six) - 3, max(ninety_six), bins), weights=np.ones_like(ninety_six)/len(ninety_six))
b.set_title("1996 relative frequency")

c.hist(o_two, np.linspace(min(o_two) - 3, max(o_two), bins), weights=np.ones_like(o_two)/len(o_two))
c.set_title("2002 relative frequency")

fig.tight_layout()
pyplot.show()

"""
b. What major differences exist among the plots for the three years?
As time went on, the number of states with high proportions of homes owned by the occupant increased.
By high, I refer to a proportion greater than 65. The right side of the graph thickened, 
and the overall relative frequency maximum decreased. 
"""

"""
c. Why do you think the plots have changed over these 17 years?
The economy improved from 1985 to 2002, so people around the country were given the purchasing power
to become landowners and not renters.
"""

"""
d. How could Congress use the information in these plots for writing tax laws that
allow major tax deductions for homeownership?
The data showed that the number of landowners increased throughout the country from 1985 to 2002.
This means that congress could be motivated to decrease taxes for landowners to encourage this trend 
to continue.
"""
