"""
3.4 The regulations of the board of health in a particular state specify that the fluoride level
must not exceed 1.5 parts per million (ppm). The 25 measurements given here represent the
fluoride levels for a sample of 25 days. Although fluoride levels are measured more than once per
day, these data represent the early morning readings for the 25 days sampled.

a. Determine the range of the measurements.
b. Dividing the range by 7, the number of subintervals selected, and rounding, we
have a class interval width of .05. Using .705 as the lower limit of the first interval,
construct a frequency histogram.
c. Compute relative frequencies for each class interval and construct a relative frequency
histogram. Note that the frequency and relative frequency histograms for
these data have the same shape.
d. If one of these 25 days were selected at random, what would be the chance (probability)
that the fluoride reading would be greater than .90 ppm? Guess (predict)
what proportion of days in the coming year will have a fluoride reading greater
than .90 ppm.
"""
import matplotlib.pyplot as pyplot
import numpy as np

df = open('./ex3-4.txt', 'r')
#a) 
data_list = []
for num in df:
    data_list.append(float(num))
print("Range: " + str(max(data_list) - min(data_list)))

#b)
fig, ((b, c)) = pyplot.subplots(nrows=1, ncols=2)
b.hist(data_list, np.linspace(0.705, max(data_list), 20))
b.set_title("Fluoride level frequency")

#c)
c.hist(data_list, np.linspace(0.705, max(data_list), 20), weights=np.ones_like(data_list)/len(data_list))
c.set_title("Fluoride level relative frequency")
fig.tight_layout()
pyplot.show()

#d)
"""
My guess is that 25% of fluoride readings will be higher than 0.90 ppm.

Based on our relative frequency graph, we can take the sum of the relative frequencies
greater than 0.9 to see the probability that any fluoride reading is greater than 0.9.
Taking this sum, we can see there is 28% chance that randomly selecting any of the 25
fluoride readings will result in a reading higher than 0.9.
"""





