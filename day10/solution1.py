import helpers

numbers = helpers.get_input_as_numbers()

def get_result():

    numbers.sort()
    numbers.append(numbers[-1]+3)
    numbers.append(0)

    last = 0
    one_count = 0
    three_count = 0

    for number in numbers:
        diff = number - last
        last = number
        if diff == 1:
            one_count = one_count + 1
        if diff == 3:
            three_count = three_count + 1

    result = one_count * three_count
    print(f"result is {one_count} * {three_count} = {result}")
    return result

result = get_result()
print("Result is: " + str(result))
