import helpers

helpers.set_directory()
lines = helpers.get_input_as_batches()

def get_result():
    result = 0

    for line in lines:
        result = result + len(set(line))

    
    return result

result = get_result()
print("Result is: " + str(result))
