import helpers

def get_result():

    # get input, add extras and sort.
    numbers = helpers.get_input_as_numbers()
    numbers.sort()
    numbers.append(numbers[-1]+3)
    numbers.append(0)
    numbers.sort()

    counter = 0
    counters = []

    # find each run of differences of 1 and _count_ how many are in a row.
    last = numbers[0]
    for number in numbers:
        diff = number - last
        last = number
        if diff == 1:
            counter += 1
        elif counter > 0:
            counters.append(counter)
            counter = 0

    # convert difference sequence scores. 3=4, 4=7. See problem.txt for details.
    for i, val in enumerate(counters):
        if val == 3:
            counters[i] = 4
        if val == 4:
            counters[i] = 7
        counters

    # multiply each score by each other score.
    result = 1
    for counter in counters:
        result = result * counter

    return result

result = get_result()
print("Result is: " + str(result))
