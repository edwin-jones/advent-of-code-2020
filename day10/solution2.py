import helpers
from functools import reduce
from collections import Counter

numbers = helpers.get_input_as_numbers()

total = 0

def get_result():

    count = len(numbers)

    counters = []
    numbers.sort()
    numbers.append(numbers[-1]+3)
    numbers.append(0)
    numbers.sort()

    counter = 0
    last = numbers[0]
    for number in numbers:
        diff = number - last
        last = number
        if diff == 1:
            counter += 1
        elif counter > 0:
            counters.append(counter)
            counter = 0

    c = Counter()
    for count in counters:
        c[count] += 1

    result = (2**c[2]) * (4**c[3]) * (7**c[4])

    return result

result = get_result()
print("Result is: " + str(result))
