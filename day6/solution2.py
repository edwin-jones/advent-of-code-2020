import helpers

helpers.set_directory()
line_batches = helpers.get_input_as_batches_of_lines()

def get_result():
    result = 0


    for lines in line_batches:

        current_set = set(lines[0])
        for line in lines:
            current_set = current_set & set(line)

        result = result + len(current_set)

    
    return result

result = get_result()
print("Result is: " + str(result))
