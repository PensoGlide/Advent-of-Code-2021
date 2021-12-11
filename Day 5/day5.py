

def getData(filePath, inInt=True):

    raw_data = open(filePath, 'r')
    data = raw_data.read()
    data = data.split('\n')
    data = [line.split(' -> ') for line in data]

    first = [line[0] for line in data]
    last = [line[1] for line in data]
    
    first_h = [line[0] for line in first]
    first_v = [line[2] for line in first]
    last_h = [line[0] for line in last]
    last_v = [line[2] for line in last]


    if inInt == True:
        first_h = [int(nr) for nr in first_h]
        first_v = [int(nr) for nr in first_v]
        last_h = [int(nr) for nr in last_h]
        last_v = [int(nr) for nr in last_v]
    
    return first_h, first_v, last_h, last_v


#first_h, first_v, last_h, last_v = getData('day5.txt', inInt=True)
first_h, first_v, last_h, last_v = getData('day5_test.txt', inInt=True)


##############################################
# Part 1

for element in range(len(first_h)):
    if 
print(first_h, last_v)