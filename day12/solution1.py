import helpers


def get_position(x, y, orders):

  directions = ['N', 'E', 'S', 'W']
  current_dir_index = 1

  for order in orders:
    direction = order[0]
    distance = order[1]

    x_multiplier = 0
    y_multiplier = 0
    turns = int(distance / 90)

    if direction == 'F':
      direction = directions[current_dir_index]

    if direction == 'R':
      for turn in range(turns):
        current_dir_index = current_dir_index + 1
        if current_dir_index > 3:
          current_dir_index = 0
        direction = directions[current_dir_index]
      continue
      
    if direction == 'L':
      for turn in range(turns):
        current_dir_index = current_dir_index - 1
        if current_dir_index < 0:
          current_dir_index = len(directions) -1
        direction = directions[current_dir_index]
      continue

    if direction == 'N':
      y_multiplier = 1
      x_multiplier = 0
    if direction == 'E':
      y_multiplier = 0
      x_multiplier = 1
    if direction == 'S':
      y_multiplier = -1
      x_multiplier = 0
    if direction == 'W':
      y_multiplier = 0
      x_multiplier = -1

    x = x + (distance * x_multiplier)
    y = y + (distance * y_multiplier)

  return abs(x)+abs(y)

def get_result():
  orders = helpers.get_input_as_directions()
  result = get_position(0, 0, orders)
  return result

result = get_result()
print("Result is: " + str(result))
