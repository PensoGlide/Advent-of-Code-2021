import requests

def getData(filePath):

    raw_data = open(filePath, 'r')
    data = raw_data.read()
    data = data.split('\n')
    
    return data

data = getData('day1.txt')

##############################################
# Part 1

counter = 0
for i in range(1, len(data)):
    if int(data[i]) > int(data[i-1]):
        counter += 1

print(counter)

##############################################
# Part 2

#data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

counter = 0
for i in range(3, len(data)):
    prevSum = int(data[i-1]) + int(data[i-2]) + int(data[i-3])
    curSum = int(data[i]) + int(data[i-1]) + int(data[i-2])

    if curSum > prevSum:
        counter += 1

print(counter)