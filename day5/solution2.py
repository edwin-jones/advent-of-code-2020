import helpers

helpers.set_directory()
lines = helpers.get_input_as_lines()

def get_results():
    results = []

    for line in lines:
        col = 0
        row = 0

        col_string = line[-3:]
        row_string = line[:-3]

        iterations = 6
        for char in row_string:
            if char == 'B':
                col = col | 1 << iterations
            iterations = iterations - 1

        iterations = 2 
        for char in col_string:
            if char == 'R':
                row = row | 1 << iterations
            iterations = iterations - 1

    
        current_value = int(col * 8 + row)
        results.append(current_value)
    
    return results

results = get_results()
results.sort()

previous = 2**32
for result in results:
    if result > previous + 1:
        print("Result: " + str(result-1))
    previous = result