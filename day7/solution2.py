import helpers

lines = helpers.get_input_as_lines()

class Bag:
    def __init__(self, color):
        self.color = color
        self.contents = {}

total = 0
def count_bag(bags, bag, previous = 1):
    global total
    for key, value in bag.contents.items():
        current = previous * value
        total = total + current
        count_bag(bags, bags[key], current)

def get_result():

    bags = {}

    for line in lines:
        pos = line.index(' ')
        current_color = line[:line.index(' ', pos + 1)]

        bag = Bag(current_color)

        if "no other bags" not in line:
            contents = line.split("contain",1)[1].split(',')

            for item in contents:
                tokens = item.strip().split(' ')
                bag.contents[tokens[1] + " " + tokens[2]] = int(tokens[0])

        bags[bag.color] = bag


    target_color = "shiny gold"
    bag = bags[target_color]

    result = count_bag(bags, bag)

    return result

get_result()
print("Result is: " + str(total))
