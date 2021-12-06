

def getData(filePath):

    raw_data = open(filePath, 'r')
    data = raw_data.read()
    data = data.split(',')
    
    return data

input = getData('day6.txt')
input = getData('day6_test.txt')

##############################################
# Part 1

data = [int(nr) for nr in input]

for day in range(1,81):
    for index in range(len(data)):
        data[index] -= 1

        if data[index] == -1:
            data.append(8)
            data[index] = 6

print(len(data))


##############################################
# Part 2

data = [int(nr) for nr in input]

ages = [data.count(i) for i in range(9)] # Conta quantos peixes têm a idade i

for i in range(256):

    ages = ages[1:]+[ages[0]] # Passa cada coluna de idades para a direita
    ages[6] += ages[-1]       # Criamos (ao somar) novos peixes com idades de 6


print(sum(ages))

