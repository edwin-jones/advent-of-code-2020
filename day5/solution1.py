import helpers

def get_result():
    result = 0
    lines = helpers.get_input_as_lines()
    translation = str.maketrans({'B': '1', 'R': '1', 'F': '0', 'L': '0'})

    for line in lines:
        binary = line.translate(translation)

        row = int(binary[:-3], 2)
        col = int(binary[-3:], 2)

        current_value = row * 8 + col

        if current_value > result:
            result = current_value

    return result

result = get_result()
print("Result is: " + str(result))