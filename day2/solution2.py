import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

lines = []

with open('./input.txt','r') as input:
    for line in input:
        lines.append(line)

def get_result():
    count = 0
    for line in lines:

        tokens = line.split(" ")

        numbers = tokens[0]
        firstIndex = int(numbers.split("-")[0]) - 1
        lastIndex = int(numbers.split("-")[1]) - 1

        char = tokens[1].replace(":", "")

        target = tokens[2]

        occurances = (1 if target[firstIndex] == char else 0 ) + (1 if target[lastIndex] == char else 0 )

        if occurances > 0 and occurances < 2:
            count = count + 1
    
    return count

result = get_result()
print("Result is: " + str(result))
