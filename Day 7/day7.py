import numpy as np
import matplotlib.pyplot as plt
import statistics as stat

def getData(filePath, inInt=False):

    raw_data = open(filePath, 'r')
    data = raw_data.read()
    data = data.split(',')

    if inInt == True:
        data = [int(nr) for nr in data]
    
    return data

inputData = getData('day7.txt', inInt=True)
#inputData = getData('day7_test.txt', inInt=True)


##############################################
# Part 1

def distance(data, mean_value): 

    fuel = 0

    for element in data:
        fuel += np.abs(element - mean_value)

    return fuel

median = stat.median(inputData)

print(distance(inputData, median))


##############################################
# Part 2
import math

def distance(data, mean_value): 

    fuel = 0

    for element in data:
        abs = np.abs(element - mean_value)
        fuel += (abs**2 + abs)/2                # Follows tringule numbers
        #fuel += round( (abs**2 + abs)/2 )

    return fuel

mean = stat.mean(inputData)

print(mean)
# 99053183 is too high
# 99053041 is too low
print(distance(inputData, 504))