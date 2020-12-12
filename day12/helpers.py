import os

def set_directory():
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

def get_input_as_moves():
    set_directory()
    moves = []

    with open('./input.txt','r') as input:
        for line in input:
            line = line.replace('\n', '')
            moves.append([line[0], int(line[1:])])

    return moves

class Vector():
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def  __add__(self, other):
    x = self.x + other.x
    y = self.y + other.y
    return Vector(x,y)

  def  __sub__(self, other):
    x = self.x - other.x
    y = self.y - other.y
    return Vector(x,y)