import helpers

def get_results():
    results = []
    lines = helpers.get_input_as_lines()
    translation = str.maketrans({'B': '1', 'R': '1', 'F': '0', 'L': '0'})

    for line in lines:
        binary = line.translate(translation)

        row = int(binary[:-3], 2)
        col = int(binary[-3:], 2)

        current_value = row * 8 + col
        results.append(current_value)

    return results

results = get_results()
results.sort()

previous = 2**32
for result in results:
    if result > previous + 1:
        print("Result: " + str(result-1))
    previous = result