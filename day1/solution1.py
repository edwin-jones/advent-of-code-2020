import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

numbers = []

with open('./input.txt','r') as input:
    for line in input:
        numbers.append(int(line))

def get_result():
    for x in numbers:
        for y in numbers:
            if x + y == 2020:
                return x*y
    
    return 0

result = get_result()

if result == 0:
    raise Exception("no valid result found")
else:
    print("Result is: " + str(result))
