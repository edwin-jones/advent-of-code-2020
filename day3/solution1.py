import helpers

helpers.set_directory()
lines = helpers.get_input_as_lines()

def get_result():
    count = 0
    x = 0

    for line in lines:

        char = line[x]
        
        if(char == '#'):
            count = count + 1

        length = len(line) - 1
        x = (x + 3) % length
    
    return count

result = get_result()
print("Result is: " + str(result))
