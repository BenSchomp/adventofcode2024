
def findWord( startY, startX, word ):
  global grid, width, height
  count = 0
  for dx in [-1,0,1]:
    for dy in [-1,0,1]:
      if dx == 0 and dy == 0:
        continue

      x = startX
      y = startY
      curWord = grid[y][x]

      x += dx
      y += dy
      while( x > -1 and y > -1 and x < width and y < height ):
        curWord += grid[y][x]
        if curWord == word:
          count += 1
          break

        if curWord != word[:len(curWord)]:
          break

        x += dx
        y += dy

  return count

def findWord2( y, x ):
  global grid, width, height

  if x <= 0 or x >= width-1 or y <= 0 or y >= height-1:
    return 0

  if not( (grid[y-1][x+1] == 'M' and grid[y+1][x-1] == 'S') or\
          (grid[y-1][x+1] == 'S' and grid[y+1][x-1] == 'M') ):
    return 0

  if not( (grid[y+1][x+1] == 'M' and grid[y-1][x-1] == 'S') or\
          (grid[y+1][x+1] == 'S' and grid[y-1][x-1] == 'M') ):
    return 0

  return 1

#--- main ---
grid = []

file = open('day-04.txt', 'r')
for line in file:
  row = []
  for c in line.strip():
    row.append(c)
  grid.append(row)
file.close()

width = len(grid[0])
height = len(grid)

part_one = part_two = 0
for r in range(height):
  for c in range(width):
    if grid[r][c] == 'X':
      part_one += findWord( r, c, 'XMAS' )
    if grid[r][c] == 'A':
      part_two += findWord2( r, c )

print( part_one )
print( part_two )

