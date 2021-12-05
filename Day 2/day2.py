

def getData(filePath):

    raw_data = open(filePath, 'r')
    data = raw_data.read()
    data = data.split('\n')
    
    return data

data = getData('day2.txt')

##############################################
# Part 1

#data = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']

horizontal = 0
depth = 0

for line in data:
    data_split = line.split(' ')

    if data_split[0] == 'forward':
        horizontal += int(data_split[1])

    elif data_split[0] == 'up':
        depth -= int(data_split[1])

    elif data_split[0] == 'down':
        depth += int(data_split[1])

print(horizontal*depth)


##############################################
# Part 2

#data = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']

horizontal = 0
depth = 0
aim = 0

for line in data:
    data_split = line.split(' ')

    if data_split[0] == 'forward':
        horizontal += int(data_split[1])
        depth += aim * int(data_split[1])

    elif data_split[0] == 'up':
        #depth -= int(data_split[1])
        aim -= int(data_split[1])

    elif data_split[0] == 'down':
        #depth += int(data_split[1])
        aim += int(data_split[1])

    #print(aim , depth, horizontal)

print(horizontal*depth)