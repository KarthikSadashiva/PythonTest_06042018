'''This is the 5th question of the test. The inputs are liquid weight of 16 
twelve-ounce cans, The desired output is printing the frequency distribution and 
calculating the summary statistics of the data such as Mean, Median and Mode.'''
import numpy as np
from scipy import stats 

weight = np.array([11.95, 11.91, 11.86, 11.94, 12.00, 11.93, 12.00, 11.94, 
          12.10, 11.95, 11.99, 11.94, 11.89, 12.01, 11.99, 11.94])

mean = np.mean(weight)
median = np.median(weight)
mode = stats.mode(weight)

max_weight = max(weight)
min_weight = min(weight)
start = 11.85
gap = 0.05
frequency = np.zeros(len(weight))
for i in range(len(weight)):
    if(weight[i]>=start and weight[i]<(start+gap)):
        frequency[i] += 1
    start += gap

print("The mean is ", mean, " The mode is ", mode, "The median is ", median)
