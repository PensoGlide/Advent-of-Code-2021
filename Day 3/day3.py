import numpy as np

def getData(filePath, inInt=False):

    raw_data = open(filePath, 'r')
    data = raw_data.read()
    data = data.split('\n')

    if inInt == True:
        data = [int(nr) for nr in data]
    
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
        if element >= 0.5:
            common.append(1)
            uncommon.append(0)
        else:
            common.append(0)
            uncommon.append(1)

    common = ''.join(map(str,common))
    uncommon = ''.join(map(str,uncommon))

    return common, uncommon

common, uncommon = getCommon_Uncommon(data)

gamma   = int(common,2)
epsilon = int(uncommon,2)


print(gamma*epsilon)


##############################################
# Part 2


def oxygen_generator_rating(data):

    common, uncommon = getCommon_Uncommon(data)
    common_bit = int(common[0])
    first_bits = np.array([ int(val[0]) for val in data])
    mask = np.ma.masked_equal(first_bits, common_bit).mask
    data = np.array(data)
    numbers = data[mask]


    for i in range(1,len(data[0])):
        print(numbers)

        if len(numbers) == 1:
            return numbers

        else:
            common, uncommon = getCommon_Uncommon(numbers)
            print(common, i)
            if common[i] == 3:
                common_bit = 1
            else:
                common_bit = int(common[i])
            first_bits = [ int(val[i]) for val in numbers]

            mask = np.ma.masked_equal(first_bits, common_bit).mask

            print(first_bits, common_bit, mask)
        
        numbers = np.array(numbers)
        numbers = numbers[mask]

    return numbers



def CO2_rating(data):

    common, uncommon = getCommon_Uncommon(data)
    common_bit = int(uncommon[0])
    first_bits = np.array([ int(val[0]) for val in data])
    mask = np.ma.masked_equal(first_bits, common_bit).mask
    data = np.array(data)
    numbers = data[mask]


    for i in range(1,len(data[0])):
        print(numbers)

        if len(numbers) == 1:
            return numbers

        else:
            common, uncommon = getCommon_Uncommon(numbers)
            print(common, i)
            if uncommon[i] == 3:
                common_bit = 1
            else:
                common_bit = int(uncommon[i])
            first_bits = [ int(val[i]) for val in numbers]

            mask = np.ma.masked_equal(first_bits, common_bit).mask

            print(first_bits, common_bit, mask)
        
        numbers = np.array(numbers)
        numbers = numbers[mask]

    return numbers


ox  = oxygen_generator_rating(data)
co2 = CO2_rating(data)

ox   = int(ox[0],2)
co2  = int(co2[0],2)

print(ox, co2)

print(ox*co2)
