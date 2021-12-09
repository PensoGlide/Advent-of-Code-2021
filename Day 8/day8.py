

def getData(filePath, allInOne=False):

    raw_data = open(filePath, 'r')
    data = raw_data.read()
    data = data.split('\n')

    output = []
    signal = []

    for line in data:
        line = line.split(' | ')
        signal_line = line[0]
        output_line = line[1]
        signal_line = signal_line.split(' ')
        output_line = output_line.split(' ')

        if allInOne == True:

            for sig in signal_line:
                signal.append(sig)

            for out in output_line:
                output.append(out)

        else:
            signal.append(signal_line)
            output.append(output_line)


    return signal, output

signal, output = getData('day8.txt', allInOne=True)
#signal, output = getData('day8_test.txt', inInt=True)
#print(signal, output)


##############################################
# Part 1

len_1 = 2
len_4 = 4
len_7 = 3
len_8 = 7
recognizable_lengths = [len_1, len_4, len_7, len_8]

count = 0

for digit in output:
    if len(digit) in recognizable_lengths:
        count += 1

print(count)




##############################################
# Part 2

signal, output = getData('day8.txt', allInOne=False)

dict = {'0': '', '1': '','2': '', '3': '', '4': '', '5': '', '6': '', '7': '', '8': '', '9': ''}
results = 0

i = -1
for line in signal:

    removed = []

    # Check for obvious numbers
    for element in line:

        # The obvious ones
        if len(element) == len_7:
            dict['7'] = "".join(sorted(element))
            removed.append(element)
        elif len(element) == len_1:
            dict['1'] = "".join(sorted(element))
            removed.append(element)
        elif len(element) == len_4:
            dict['4'] = "".join(sorted(element))
            removed.append(element)
        elif len(element) == len_8:
            dict['8'] = "".join(sorted(element))
            removed.append(element)

        #print(line, element, len(element))
        #print(dict)

    
    # Check for letters that make up each number
    c_f = []
    for letter in dict['7']:
        if letter not in dict['1']:
            a = letter
        else:
            c_f.append(letter)

    b_d = []
    for letter in dict['4']:
        if letter not in dict['1']:
            b_d.append(letter)

    e_g = []
    for letter in dict['8']:
        if letter not in (dict['1'] + dict['4'] + dict['7']):
            e_g.append(letter)


    # Check for the rest of the numbers
    [line.remove(number) for number in removed]

    for element in line:
        if all(item in element for item in c_f) and all(item in element for item in e_g):
            dict['0'] = "".join(sorted(element))
            line.remove(element)

    for element in line:
        if all(item in element for item in b_d) and all(item in element for item in c_f):
            dict['9'] = "".join(sorted(element))
            line.remove(element)
            for letter in e_g:
                if letter in dict['9']:
                    g = letter
                else:
                    e = letter


    for element in line:
        if all(item in element for item in c_f) and (e not in element):
            dict['3'] = "".join(sorted(element))
            line.remove(element)
            for letter in b_d:
                if letter not in dict['3']:
                    b = letter
                else:
                    d = letter

    
    for element in line:
        if all(item in element for item in e_g) and (b not in element):
            dict['2'] = "".join(sorted(element))
            line.remove(element)
            for letter in c_f:
                if letter not in element:
                    f = letter
                else:
                    c = letter

    
    for element in line:
        if e in element:
            dict['6'] = "".join(sorted(element))
        else:
            dict['5'] = "".join(sorted(element))


    # Determine result
    i += 1
    result = ''
    for element in output[i]:
        element = "".join(sorted(element))
        for key, value in dict.items():
            if element == value:
                result += key
    
    results += int(result)


print(results)
    
