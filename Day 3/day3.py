import numpy as np

def getData(filePath):

    raw_data = open(filePath, 'r')
    data = raw_data.read()
    data = data.split('\n')
    
    return data

data = getData('day3.txt')
#data = getData('day3_test.txt')


##############################################
# Part 1

def getCommon_Uncommon(data): 

    result = np.zeros((1, len(list(data[0]))), dtype=float )
    common = []
    uncommon = []

    for line in data:
        dataSplit = np.array([ int(a) for a in list(line) ])
        result += dataSplit/ len(data)

    for element in result[0]:
        print(element)
        if element > 0.5:
            common.append(1)
            uncommon.append(0)
        else:
            common.append(0)
            uncommon.append(1)

    common = ''.join(map(str,common))
    uncommon = ''.join(map(str,uncommon))

    return common, uncommon

gamma, epsilon = getCommon_Uncommon(data)

gamma   = int(gamma,2)
epsilon = int(epsilon,2)


print(gamma*epsilon)


##############################################
# Part 2
