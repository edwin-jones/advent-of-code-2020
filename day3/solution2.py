import helpers
import functools
import operator

helpers.set_directory()
lines = helpers.get_input_as_lines()

def get_result(x_offset, y_offset):
    count = 0
    x = 0

    for idx, line in enumerate(lines):

        if(idx % y_offset != 0):
            continue

        char = line[x]
        
        if(char == '#'):
            count = count + 1

        length = len(line) - 1
        x = (x + x_offset) % length
    
    return count

results = []
results.append(get_result(1,1))
results.append(get_result(3,1))
results.append(get_result(5,1))
results.append(get_result(7,1))
results.append(get_result(1,2))

result = functools.reduce(operator.mul, results)
print("Result is: " + str(result))
