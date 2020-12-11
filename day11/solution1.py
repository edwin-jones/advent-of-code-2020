import helpers

grid = helpers.get_input_as_lines()
rows = len(grid)
cols = len(grid[0])

neighbours = [
  [1, 1],   #NE
  [-1, -1], #SW
  [1, 0],   #E
  [0, 1],   #N
  [0, -1],  #S
  [-1, 0],  #W
  [1, -1],  #SE
  [-1, 1]   #NW
]

def get_neighbour_count(x, y, grid):

  count = 0

  for neighbour in neighbours:
    [xOffset, yOffset] = neighbour

    targetX = x + xOffset
    targetY = y + yOffset

    if targetX > 0 and targetX < cols and targetY > 0 and targetY < rows:
      if grid[targetX][targetY] == '#':
        count = count + 1

  return count

def update_cells():
  old_grid = grid.copy()
  for y in range(rows):
    for x in range(cols):
      neighbour_count = get_neighbour_count(x, y, old_grid)
      cell = old_grid[y][x]

      if cell == 'L' and neighbour_count == 0:
        grid[y] = grid[y][:x] + '#' + old_grid[y][x+1:]
      
      if cell == '#' and neighbour_count > 3:
        grid[y] = grid[y][:x] + 'L' + old_grid[y][x+1:]


def get_result():

    update_cells()
    for line in grid:
      print(line)
    return 0

result = get_result()
print("Result is: " + str(result))
