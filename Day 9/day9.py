import numpy as np

def getData(filePath):

    raw_data = open(filePath, 'r')
    data = raw_data.read()
    data = data.split('\n')

    #if inInt == True:
    #    data = [int(nr) for nr in data]
    
    return data

data = getData('day9.txt')
#data = getData('day9_test.txt')


##############################################
# Part 1


matrix = np.ones((len(data[0])+2,), dtype=int)*9
#print(matrix)
for line in data:

    line = list(line)
    row = np.array(line, dtype=int)
    row = np.insert(row, 0, 9)
    row = np.append(row, 9)
    matrix = np.vstack([matrix, row])

row = np.ones((len(data[0])+2,), dtype=int)*9
matrix = np.vstack([matrix, row])
#print(matrix)


minima = []
x = []
y = []
for j in range(1, len(row)-1):
    for i in range(1, len(matrix)-1):

        if (matrix[i][j] < matrix[i-1][j]) and (matrix[i][j] < matrix[i+1][j]) and (matrix[i][j] < matrix[i][j+1]) and (matrix[i][j] < matrix[i][j-1]):
            minima.append(matrix[i][j])
            x.append(i)
            y.append(j)

print(minima)
print(sum(minima)+len(minima))





##############################################
# Part 2


basins_x = []
basins_y = []
for min in range(len(minima)):
    #print(min)

    x_loc = [x[min]]
    y_loc = [y[min]]
    #print(x_loc)
    #print(y_loc)

    zero = np.ones((len(data)+2,len(data[0])+2))*9
    for j in range(len(zero[0])):
        for i in range(len(zero)):
            zero[i][j] = -1.
    #print(zero)


    index = 0
    while index != len(x_loc):
        i = x_loc[index]
        j = y_loc[index]
        #print(index)

        zero[i][j] = matrix[i][j]

        index += 1

        if ((matrix[i-1][j] == matrix[i][j] + 1) or (matrix[i-1][j] == matrix[i][j])) and (matrix[i-1][j] < 9) and (matrix[i-1][j] != zero[i-1][j]):
            x_loc.append(i-1)
            y_loc.append(j)
            zero[i-1][j] = matrix[i-1][j]
                
        if ((matrix[i+1][j] == matrix[i][j] + 1)  or (matrix[i+1][j] == matrix[i][j])) and (matrix[i+1][j] < 9) and (matrix[i+1][j] != zero[i+1][j]):
            x_loc.append(i+1)
            y_loc.append(j)
            zero[i+1][j] = matrix[i+1][j]

        if ((matrix[i][j+1] == matrix[i][j] + 1) or (matrix[i][j+1] == matrix[i][j])) and (matrix[i][j+1] < 9) and (matrix[i][j+1] != zero[i][j+1]):
            x_loc.append(i)
            y_loc.append(j+1)
            zero[i][j+1] = matrix[i][j+1]
                
        if ((matrix[i][j-1] == matrix[i][j] + 1) or (matrix[i][j-1] == matrix[i][j])) and (matrix[i][j-1] < 9) and (matrix[i][j-1] != zero[i][j-1]):
            x_loc.append(i)
            y_loc.append(j-1)
            zero[i][j-1] = matrix[i][j-1]
            #print(matrix)
            #print(i, j)
            #print(matrix[i][j-1], matrix[i][j])
            #exit(0)

        #print(x_loc, y_loc)
        #print(zero)

    basins_x.append(x_loc)
    basins_y.append(y_loc)

#print(basins_x)

lengths = []
for basin in basins_x:
    lengths.append(len(basin))

sorted_lengths = sorted(lengths)
print(sorted_lengths)

result = 1
for number in sorted_lengths[-3:]:
    result *= number

print(result)


##########################################################



import networkx as nx
import math

with open('day9_test.txt') as f:
    area = nx.Graph()
    for y, line in enumerate(f.readlines()):
        for x, depth in enumerate(line.strip()):
            area.add_node((x, y))
            if x > 0:
                area.add_edge((x, y), (x-1, y))
            if y > 0:
                area.add_edge((x, y), (x, y-1))
            area.nodes[(x, y)]['depth'] = depth

print(area.nodes)
for x, y in area.nodes:
    if area.nodes[(x, y)]['depth'] == '9':
        area.remove_edges_from([
            ((x, y), (x-1, y)),
            ((x, y), (x+1, y)),
            ((x, y), (x, y-1)),
            ((x, y), (x, y+1))
        ])

component_sizes = [len(c) for c in sorted(nx.connected_components(area), key=len, reverse=True)]

print(math.prod(component_sizes[:3]))