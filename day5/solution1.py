import helpers

helpers.set_directory()
lines = helpers.get_input_as_lines()

def get_result():
    result = 0
    x = 0
    error = False



    for line in lines:
        col_max = 128
        col_min = 0
        col = 0

        row_min = 0
        row_max = 8
        row = 0

        col_string = line[-3:]
        row_string = line[:-3]

        iterations = 7
        for char in row_string:
            if char == 'F':
                col_max = col_max - (2**iterations) / 2
                col = col_max - 1
            if char == 'B':
                col_min = col_min + (2**iterations) / 2
                col = col_min
            iterations = iterations - 1

        iterations = 3 
        for char in col_string:
            if char == 'L':
                row_max = row_max - (2**iterations) / 2
                row = row_max - 1
            if char == 'R':
                row_min = row_min + (2**iterations) / 2
                row = row_min
            iterations = iterations - 1

    
        current_value = int(col * 8 + row)
        print(current_value)

        if current_value > result:
            result = current_value
    
    return result

result = get_result()
print("Result is: " + str(result))
