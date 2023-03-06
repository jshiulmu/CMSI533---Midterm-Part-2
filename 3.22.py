"""
3.22 A study of the survival times, in days, of skin grafts on burn patients was examined by
Woolson and Lachenbruch [Biometrika (1980) 67:597-606]. Two of the patients left the study
prior to the failure of their grafts. The survival time for these individuals is some number greater
than the reported value.
Survival time (days): 37, 19, 57*, 93, 16, 22, 20, 18, 63, 29, 60*
(The “*" indicates that the patient left the study prior to failure of the graft; values given are for
the day the patient left the study.)

a. Calculate the measures of center (if possible) for the 11 patients.
b. If the survival times of the two patients who left the study were obtained, how
would these new values change the values of the summary statistics calculated
in (a)?
"""

import numpy as np

df = open('./ex3-22.txt', 'r')

#a
data_set = []
for num in df:
    data_set.append(int(num))
data_set.sort()
def summary(data):
    mean = str(np.mean(data))
    mode = "None"
    median = str(np.median(data))
    return "Mean: " + mean + " | " + " Mode: " + mode + " | " + " Median: " + median
print(summary(data_set))

"""
b. If the survival times of the two patients who left the study were obtained, how
would these new values change the values of the summary statistics calculated
in (a)?

The sorted dataset is: [16, 18, 19, 20, 22, 29, 37, 57*, 60*, 63, 93], where 57 and 60 are incomplete
datapoints. This means, in truth, their value is supposed to be higher. If the true survival times
of these patients were obtained, the measures of center would change in the following ways:
- Mean: mean would increase.
- Mode: if the two datapoints were equal to 63 or 93, the mode would then become
whichever data point repeated. For example, if the 57 datapoint became 63, and 60 became
70, then the mode would exist, and the mode would be 63.
- Median: the median would not change.
"""