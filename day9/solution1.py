import helpers


preamble_length = 25
numbers = helpers.get_input_as_numbers()

def get_result():

    length = len(numbers)

    while length > preamble_length:
        length = length - 1

        preamble = numbers[:preamble_length]
        item = numbers[preamble_length:][0]

        found = True
        for x in preamble:
            for y in preamble:
                test = x + y
                if test == item:
                    found = False
        if found:
            return item

        numbers.pop(0)
        

    return 0

result = get_result()
print("Result is: " + str(result))
