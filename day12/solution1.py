import helpers
from copy import copy

class Position():
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
  

def apply_moves(start_position, moves):
  final_position = copy(start_position)

  directions = ['N', 'E', 'S', 'W']
  current_dir_index = 1

  for move in moves:
    direction = move[0]
    distance = move[1]

    x_multiplier = 0
    y_multiplier = 0
    turns = int(distance / 90)

    if direction == 'F':
      direction = directions[current_dir_index]

    if direction == 'R':
      for _ in range(turns):
        current_dir_index = current_dir_index + 1
        if current_dir_index > 3:
          current_dir_index = 0
        direction = directions[current_dir_index]
      continue
      
    if direction == 'L':
      for _ in range(turns):
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

    final_position.x = final_position.x + (distance * x_multiplier)
    final_position.y = final_position.y + (distance * y_multiplier)

  return final_position

def get_result():
  moves = helpers.get_input_as_moves()
  start_position = Position()
  final_position = apply_moves(start_position, moves)
  result = abs(final_position.x) + abs(final_position.y)
  return result

result = get_result()
print("Result is: " + str(result))
