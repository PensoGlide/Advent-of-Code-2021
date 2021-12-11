import math

def getData(filePath):

    raw_data = open(filePath, 'r')
    data = raw_data.read()
    data = data.split('\n')
    
    return data

data = getData('day10.txt')
#data = getData('day10_test.txt')


##############################################
# Part 1


line_wrong = []
potential_incomplete = []

for line in data:

    corrupted = False

    opening = []
    closing = []
    map = {'(': 0, ')': 0, '[': 1, ']': 1, '{': 2, '}': 2, '<': 3, '>': 3}

    for element in line:
        #print(line, element)

        if element == '(' or element == '[' or element == '{' or element == '<':
            opening.append(element)
        elif element == ')' or element == ']' or element == '}' or element == '>':
            closing.append(element)
        
        if len(closing) > 0:
            if map[closing[-1]] != map[opening[-1]]:
                line_wrong.append(closing[-1])
                corrupted = True
                break
            else:
                opening.pop(-1)
                closing.pop(-1)

    if corrupted == False:
        potential_incomplete.append(line)

#print(line_wrong)

points = {')': 3, ']': 57, '}': 1197, '>': 25137}
total = 0


for error in line_wrong:
    total += points[error]
        
print(total)


##############################################
# Part 2

points_line = []
incomplete_line = []

for line in potential_incomplete:

    points = []
    incomplete = []
    
    opening = []
    closing = []
    map = {'(': 1, ')': 1, '[': 2, ']': 2, '{': 3, '}': 3, '<': 4, '>': 4}

    for element in line:
        #print(line, element)

        if element == '(' or element == '[' or element == '{' or element == '<':
            opening.append(element)
        elif element == ')' or element == ']' or element == '}' or element == '>':
            closing.append(element)

        if len(closing) > 0:
            if map[closing[-1]] != map[opening[-1]]:
                line_wrong.append(closing[-1])
                corrupted = True
                break
            else:
                opening.pop(-1)
                closing.pop(-1)

    if len(opening) > 0:
        for i in range(len(opening)-1 , -1, -1):
            incomplete.append(opening[i])
            points.append(map[opening[i]])

        incomplete_line.append(incomplete)
        points_line.append(points)

#print(incomplete_line)


line_total = []

for points in points_line:

    total = 0
    for point in points:
        total *= 5
        total += point

    line_total.append(total)

line_total = sorted(line_total)
#print(line_total)

middle = math.ceil(len(line_total)/2)-1
#print(middle)
print(line_total[middle])