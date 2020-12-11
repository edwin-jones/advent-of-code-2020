import helpers
import math

grid = helpers.get_input_as_lines()
rows = len(grid)
cols = len(grid[0])

neighbours = [
  [1, 1],   #SE -+
  [-1, -1], #NW 
  [1, 0],   #E -
  [0, 1],   #S -+
  [0, -1],  #N
  [-1, 0],  #w
  [1, -1],  #NE
  [-1, 1]   #SW -+
]

updated = True

def get_neighbour_count(x, y, grid):

  count = 0

  for neighbour in neighbours:
    [x_offset, y_offset] = neighbour

    for i in range(2**32):
      if i == 0:
        continue
      target_x = x + (x_offset*i)
      target_y = y + (y_offset*i)

      if(target_x >= cols or target_x < 0):
        break

      if(target_y >= rows) or target_y < 0:
        break

      if target_x >= 0 and target_x < cols and target_y >= 0 and target_y < rows:
        if grid[target_y][target_x] == '#':
          count = count + 1
          break
        if grid[target_y][target_x] == 'L':
          break

  return count

def update_cells():
  global updated
  old_grid = grid.copy()
  for y in range(rows):
    for x in range(cols):

      if x == 5 and y == 0:
        foo = 3333

      neighbour_count = get_neighbour_count(x, y, old_grid)
      cell = old_grid[y][x]

      if cell == 'L' and neighbour_count == 0:
        grid[y] = grid[y][:x] + '#' + old_grid[y][x+1:]
        updated = True
      
      if cell == '#' and neighbour_count > 4:
        grid[y] = grid[y][:x] + 'L' + old_grid[y][x+1:]
        updated = True

def print_grid():
    for line in grid:
      print(line)

    print()

def get_result():

    global updated
    
    while updated:
      updated = False
      update_cells()

    print_grid()

    result = 0
    for row in grid:
      result = result + row.count('#')

    return result

result = get_result()
print("Result is: " + str(result))
