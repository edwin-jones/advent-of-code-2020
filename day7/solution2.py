import helpers

lines = helpers.get_input_as_lines()

class Bag:
    def __init__(self, color):
        self.color = color
        self.contents = {}

total = 0
bags = {}

def count_bags(bag, previous = 1):
    global total
    for key, value in bag.contents.items():
        current = previous * value
        total = total + current
        count_bags(bags[key], current)

def get_result():
    for line in lines:
        words = line.split(' ')
        current_color = f"{words[0]} {words[1]}"

        bag = Bag(current_color)

        if "no other bags" not in line:
            items = line.split("contain",1)[1].split(',')

            for item in items:
                tokens = item.strip().split(' ')
                bag.contents[f"{tokens[1]} {tokens[2]}"] = int(tokens[0])

        bags[bag.color] = bag


    target_color = "shiny gold"
    root_bag = bags[target_color]

    result = count_bags(root_bag)
    return result

get_result()
print("Result is: " + str(total))
