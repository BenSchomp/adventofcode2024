
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
      #print( x, y, grid[y][x] )

      x += dx
      y += dy
      while( x > -1 and y > -1 and x < width and y < height ):
        #print( x, y, grid[y][x] )
        curWord += grid[y][x]
        if curWord == word:
          count += 1
          #print( 'match!')
          break

        if curWord != word[:len(curWord)]:
          #print( 'no match')
          break

        x += dx
        y += dy
      #print( '-' )

  return count

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

part_one = 0
for r in range(height):
  for c in range(width):
    if grid[r][c] == 'X':
      part_one += findWord( r, c, 'XMAS' )


print( part_one )
