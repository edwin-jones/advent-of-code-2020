import helpers

combinations = set()

def get_combinations(combination):
    for i, current in enumerate(combination):
        if combination[2]==3:
            test=1
        j = i+2
        if j >= len(combination):
            break
        future = combination[j]
        diff = future - current
        prev = current

        if(diff <= 3):
            new_combination = combination.copy()
            new_combination.remove(combination[i+1])
            get_combinations(new_combination)

    thing = str(combination)
    if thing not in combinations:
        combinations.add(thing)
        print(len(combinations))



def get_result():

    # get input, add extras and sort.
    numbers = helpers.get_input_as_numbers()
    numbers.sort()
    numbers.append(numbers[-1]+3)
    numbers.append(0)
    numbers.sort()

    get_combinations(numbers)

    return len(combinations)

result = get_result()
print("Result is: " + str(result))
