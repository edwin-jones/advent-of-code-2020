import helpers
from copy import copy

class Position():
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

class Ship():
  directions = ['N', 'E', 'S', 'W']

  def __init__(self):
    self.position = Position()
    self.current_direction_index = 1
  
  def apply_move(self, move):
    direction = move[0]
    distance = move[1]

    x_multiplier = 0
    y_multiplier = 0
    turns = int(distance / 90)

    if direction == 'F':
      direction = self.directions[self.current_direction_index]

    if direction == 'R':
      for _ in range(turns):
        self.current_direction_index = self.current_direction_index + 1
        if self.current_direction_index > 3:
          self.current_direction_index = 0
        direction = self.directions[self.current_direction_index]
      return
      
    if direction == 'L':
      for _ in range(turns):
        self.current_direction_index = self.current_direction_index - 1
        if self.current_direction_index < 0:
          self.current_direction_index = len(self.directions) -1
        direction = self.directions[self.current_direction_index]
      return

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

    self.position.x = self.position.x + (distance * x_multiplier)
    self.position.y = self.position.y + (distance * y_multiplier)
  
def get_result():
  moves = helpers.get_input_as_moves()
  ship = Ship()

  for move in moves:
    ship.apply_move(move)

  result = abs(ship.position.x) + abs(ship.position.y)
  return result

result = get_result()
print("Result is: " + str(result))
