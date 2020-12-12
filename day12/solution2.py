import helpers
from copy import copy
import pygame

class Ship():
  directions = ['N', 'E', 'S', 'W']

  def __init__(self):
    self.position = pygame.math.Vector2()
    self.current_direction_index = 1

  def __str__(self):
    return f"Ship. Dir: {self.directions[self.current_direction_index]}, x:{self.position.x}, y:{self.position.y}"

class Waypoint(Ship):
  def __str__(self):
    return f"Waypoint. Dir: {self.directions[self.current_direction_index]}, x:{self.position.x}, y:{self.position.y}"

  def apply_move(self, move, ship):
    delta = self.position - ship.position
    direction = move[0]
    distance = move[1]

    x_multiplier = 0
    y_multiplier = 0

    if direction == 'F':
      return

    if direction == 'R':
      vec = pygame.math.Vector2(delta.x,delta.y)
      vec = vec.rotate(-distance)
      self.position.x = ship.position.x + int(vec.x)
      self.position.y = ship.position.y + int(vec.y)
      return

    if direction == 'L':
      vec = pygame.math.Vector2(delta.x,delta.y)
      vec = vec.rotate(distance)
      self.position.x = ship.position.x + int(vec.x)
      self.position.y = ship.position.y + int(vec.y)
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
      waypoint.apply_move(move, ship)

  result = int(abs(ship.position.x) + abs(ship.position.y))
  return result

result = get_result()
print("Result is: " + str(result))
