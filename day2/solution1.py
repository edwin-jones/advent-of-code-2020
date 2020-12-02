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
        min = int(numbers.split("-")[0])
        max = int(numbers.split("-")[1])

        char = tokens[1].replace(":", "")

        target = tokens[2]

        occurances = target.count(char)

        if occurances >= min and occurances <= max:
            count = count + 1
    
    return count

result = get_result()
print("Result is: " + str(result))
