import helpers


target = 552655238
numbers = helpers.get_input_as_numbers()

def get_result():

    length = len(numbers)

    while length > 1:
        length = length - 1

        total = 0

        index = 0
        items = []
        while total < target:
            total += numbers[index]
            items.append(numbers[index])
            index = index + 1

        result = sum(items)
        if result == target:
            items.sort()
            a = items[0]
            b = items[-1]
            return a + b

            

        numbers.pop(0)
        

    return 0

result = get_result()
print("Result is: " + str(result))
