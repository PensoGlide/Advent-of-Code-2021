import numpy as np

def getData(filePath, inInt=True):

    raw_data = open(filePath, 'r')
    data = raw_data.read()
    data = data.split('\n')

    instructions = []
    points = []

    for line in data:
        if 'fold' in line:
            value = line.split(' ')
            instructions.append(value[-1].split('='))
        elif line == '':
            continue
        else:
            points.append( [int(number) for number in line.split(',') ])

    return points, instructions


points, instructions = getData('day13.txt')
#points, instructions = getData('day13_test.txt')
print(points)
print(instructions)


##############################################
# Part 1

n_points = []

for instruction in instructions:

    n_points = []

    for point in points:
        #print(points)
        #print(point)

        new_point = [point[0],point[1]]

        if instruction[0] == 'x':
            if point[0] > int(instruction[1]):
                new_point[0] = 2*int(instruction[1]) - point[0]
                new_point[1] = point[1]
                #print(new_point)
                

        else:
            if point[1] > int(instruction[1]):
                new_point[0] = point[0]
                new_point[1] = 2*int(instruction[1]) - point[1]
                #print(new_point)
                
        
        #points.remove(point)
        #if new_point not in points:
        #    points.append(new_point)
        if new_point not in n_points:
            n_points.append(new_point)
            points = n_points
    break

print(points)
print(len(points))



##############################################
# Part 2

n_points = []

for instruction in instructions:

    n_points = []

    for point in points:
        #print(points)
        #print(point)

        new_point = [point[0],point[1]]

        if instruction[0] == 'x':
            if point[0] > int(instruction[1]):
                new_point[0] = 2*int(instruction[1]) - point[0]
                new_point[1] = point[1]
                #print(new_point)
                

        else:
            if point[1] > int(instruction[1]):
                new_point[0] = point[0]
                new_point[1] = 2*int(instruction[1]) - point[1]
                #print(new_point)
                
        
        #points.remove(point)
        #if new_point not in points:
        #    points.append(new_point)
        if new_point not in n_points:
            n_points.append(new_point)
            points = n_points
    #break # This is to eliminate in Part 2

print(points)
print(len(points))

import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

for point in points:
    x.append(point[0])
    y.append(point[1]*-1)

plt.plot(x,y, 'ro')
#plt.imshow(points, cmap='hot', interpolation='nearest')
plt.show()
    