
def score( curX, curY ):
  global grid, width, height
  elevation = grid[curY][curX]

  for (dx, dy) in [(0,-1),(1,0),(0,1),(-1,0)]:
    newX = curX + dx
    newY = curY + dy

    if newX < 0 or newX >= width or newY < 0 or newY >= height:
      continue

    if grid[newY][newX] != elevation + 1:
      continue

    if grid[newY][newX] == 9:
      if (newX, newY) not in summits:
        summits.add( (newX, newY) )
    else:
      score( newX, newY )

def score2( curX, curY ):
  global grid, width, height
  elevation = grid[curY][curX]

  result = 0
  for (dx, dy) in [(0,-1),(1,0),(0,1),(-1,0)]:
    newX = curX + dx
    newY = curY + dy

    if newX < 0 or newX >= width or newY < 0 or newY >= height:
      continue

    if grid[newY][newX] != elevation + 1:
      continue

    if grid[newY][newX] == 9:
      result += 1
    else:
      result += score2( newX, newY )
    
  return result


# --- main ---
grid = []
trailheads = []

file = open('day-10.txt', 'r')
for line in file:
  row = []
  for col in line.strip():
    row.append(int(col))
  grid.append(row)
file.close

height = len(grid)
width = len(grid[0])

part_one = part_two = 0
for row in range(height):
  for col in range(width):
    if grid[row][col] == 0:
      summits = set()
      score( col, row )
      part_one += len(summits)
      part_two += score2( col, row )

print( part_one )
print( part_two )
