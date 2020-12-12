import helpers

class Position():
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def  __add__(self, other):
    x = self.x + other.x
    y = self.y + other.y
    return Position(x,y)

  def  __sub__(self, other):
    x = self.x - other.x
    y = self.y - other.y
    return Position(x,y)


class Ship():

  def __init__(self):
    self.position = Position()


class Waypoint(Ship):

  directions = ['N', 'E', 'S', 'W']

  def apply_move(self, move, ship_position):
    offset = self.position - ship_position
    direction = move[0]
    distance = move[1]
    turns = int(distance / 90)

    x_multiplier = 0
    y_multiplier = 0

    if direction == 'F':
      return

    if direction == 'R':
      for _ in range(turns):
        x = offset.x
        y = offset.y
        offset.x = y
        offset.y = -x
      self.position.x = ship_position.x + offset.x
      self.position.y = ship_position.y + offset.y
      return

    if direction == 'L':
      for _ in range(turns):
        x = offset.x
        y = offset.y
        offset.x = -y
        offset.y = x 
      self.position.x = ship_position.x + offset.x
      self.position.y = ship_position.y + offset.y
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
  waypoint = Waypoint()
  waypoint.position.x = 10
  waypoint.position.y = 1

  for move in moves:
    direction = move[0]
    distance = move[1]
    if direction == 'F':
      diff = waypoint.position - ship.position
      for _ in range(distance):
        ship.position = ship.position + diff
      waypoint.position = ship.position + diff

    else:
      waypoint.apply_move(move, ship.position)

  result = abs(ship.position.x) + abs(ship.position.y)
  return result

result = get_result()
print("Result is: " + str(result))
