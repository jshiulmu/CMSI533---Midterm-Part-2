"""
3.80 Although an exhaust fan is present in nearly every bathroom, it often is not used due to the
high noise level. This is an unfortunate practice because regular use of the fan results in a reduction
of indoor moisture. Excessive indoor moisture often results in the development of mold,
which may have adverse health consequences. Consumer Reports in its January 2004 issue reports
on a wide variety of bathroom fans. The following table displays the price (P) in dollars of the fans
and the quality of the fan measured in airflow (AF), cubic feet per minute (cfm).

a. Plot the data in a scatterplot and comment on the relationship between price and
airflow.
b. Compute the correlation coefficient for this data set. Is there a strong or weak
relationship between price and airflow of the fans?
c. Is your conclusion in part (b) consistent with your answer in part (a)?
d. Based on your answers in parts (a) and (b), would it be reasonable to conclude
that higher-priced fans generate greater airflow?
"""
import matplotlib.pyplot as pyplot
import numpy as np

#a
df = open('./ex3-80.txt', 'r')
price = []
airflow = []
for row in df:
    row = row.split(',')
    price.append(float(row[0]))
    airflow.append(float(row[1]))
print(price)
pyplot.scatter(price, airflow)
pyplot.xlabel("Price")
pyplot.ylabel("Airflow")
pyplot.show()

#b
correlation_coeff = np.corrcoef(price, airflow)[0][1]
print("Correlation coefficient: " + str(correlation_coeff))

"""
c. Is your conclusion in part (b) consistent with your answer in part (a)?
Yes. Price and airflow did not seem very correlated on the scatterplot, and the calculated
coefficient is closer to 0 than it is to 1.
"""

"""
d. Based on your answers in parts (a) and (b), would it be reasonable to conclude
that higher-priced fans generate greater airflow?
Very slightly. The correlation coefficient is greater than 0, which signifies a positive, direct correlation
between the variables. So, in general, higher-priced fans generate greater airflow. However, 
the value of the correlation coefficient is 0.41, which is not very high. This means that although 
high price may mean high airflow, there is a decent chance it may not. For example, there is a fan in the data
that cost $60 and generates 110 cfm in airflow.
"""
