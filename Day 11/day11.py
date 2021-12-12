import numpy as np

def getData(filePath, inInt=True):

    raw_data = open(filePath, 'r')
    data = raw_data.read()
    data = data.split('\n')

    output = []

    if inInt == True:
        for line in data:
            int_line = [int(nr) for nr in line]
            output.append(int_line)
    
    return np.matrix(output)


#data = getData('day11.txt')
data = getData('day11_test.txt')


##############################################
# Part 1


def evolution(data, iteration):

    num_rows, num_cols = data.shape
    ones = np.ones((len(data),len(data[0]))).astype(int)
    count = 0

    for step in range(iteration):

        data += ones
        cond = True

        while cond:

            nines = np.argwhere(data > 9)
            #print(nines)

            if len(nines) == 0:
                cond = False

            for nine in nines:

                for i in range(nine[0]-1, nine[0]+2, +1):
                    for j in range(nine[1]-1, nine[1]+2, +1):
                        #print(i, j)

                        if i == nine[0] and j == nine[1]:
                            data[i,j] = 0
                            #print('Nabo')
                            #print(i,j)
                        elif j >= num_cols or j < 0 or i >= num_rows or i < 0:
                            #print('Wut')
                            #print(i,j)
                            continue
                        elif data[i,j] == 0:
                            continue
                        else:
                            data[i,j] += 1
                            #print('Aconteceu')
                            #print(i,j, data)
        #print(data)
        count += len(np.argwhere(data == 0))

    return count
                    

print(evolution(data, 195))
#print(data)


##############################################
# Part 2

data = getData('day11.txt')
#data = getData('day11_test.txt')

def flash(data,iteration):

    num_rows, num_cols = data.shape
    ones = np.ones((len(data),len(data[0]))).astype(int)
    count = 0

    for step in range(iteration):

        if len(np.argwhere(data == 0)) == num_rows * num_cols:
            return step

        data += ones
        cond = True
        

        while cond:

            nines = np.argwhere(data > 9)
            #print(nines)

            if len(nines) == 0:
                cond = False

            for nine in nines:

                for i in range(nine[0]-1, nine[0]+2, +1):
                    for j in range(nine[1]-1, nine[1]+2, +1):
                        #print(i, j)

                        if i == nine[0] and j == nine[1]:
                            data[i,j] = 0
                            #print('Nabo')
                            #print(i,j)
                        elif j >= num_cols or j < 0 or i >= num_rows or i < 0:
                            #print('Wut')
                            #print(i,j)
                            continue
                        elif data[i,j] == 0:
                            continue
                        else:
                            data[i,j] += 1
                            #print('Aconteceu')
                            #print(i,j, data)
        #print(data)
        count += len(np.argwhere(data == 0))

print(flash(data,1000000))