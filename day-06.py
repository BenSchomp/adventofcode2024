
def display(grid, highlight=None):
  compass = ['N', 'E', 'S', 'W']
  for r in range(len(grid)):
    for c in range(len(grid[r])):
      x = '.'
      if grid[r][c] == 1:
        x = '#'
      if highlight and c == highlight[0] and r == highlight[1]:
        x = 'O'
        #print( c, r, highlight[0], highlight[1] )
      if grid[r][c] >= 10:
        x = compass[grid[r][c] - 10]
      print( x, end='' )
    print()
  print()

# --- main ---

grid = []

file = open('day-06.txt', 'r')
curRow = 0
for line in file:
  row = []

  curCol = 0
  for c in line.strip():
    if c == '.':
      row.append(0)
    elif c == '#':
      row.append(1)
    elif c == '^':
      (startX, startY) = (curCol, curRow)
      row.append(0)

    curCol += 1

  grid.append(row)
  curRow += 1

file.close()

width = curCol
height = curRow

# --- PART ONE ---

(x, y) = (startX, startY)
visited = set()
visited.add( (x,y) )
dir = 0 # 0: north / 1: east / 2: south / 3: west

while True:
  dx = dy = 0
  if dir == 0:
    dy = -1
  elif dir == 1:
    dx = 1
  elif dir == 2:
    dy = 1
  elif dir == 3:
    dx = -1

  x += dx
  y += dy

  if x < 0 or x >= width or y < 0 or y >= height:
    break

  if grid[y][x] == 1:
    dir = (dir+1)%4
    x -= dx
    y -= dy
  else:
    visited.add( (x,y) )

print( len(visited) )

# --- PART TWO ---

part_two = 0

for j in range(height):
  for i in range(width):
    if (j == startX and i == startY) or grid[j][i] == 1:
      continue
    else:
      grid[j][i] = 1

    #for a in range(height):
    #  for b in range(width):
    #    if grid[a][b] >= 10:
    #      grid[a][b] = 0

    (x, y) = (startX, startY)
    dir = 0
    visited = set()
    visited.add( (x,y,dir) )

    #print( 'try:', i, j )
    #print( 'visited:', visited )
    #grid[y][x] = 10
    #display(grid)

    while True:
      dx = dy = 0
      if dir == 0:
        dy = -1
      elif dir == 1:
        dx = 1
      elif dir == 2:
        dy = 1
      elif dir == 3:
        dx = -1

      x += dx
      y += dy

      if x < 0 or x >= width or y < 0 or y >= height:
        #display(grid)
        #print( "    FELL OFF")
        break

      if grid[y][x] == 1:
        dir = (dir+1)%4
        x -= dx
        y -= dy

        #print(x,y,dir)
        #display(grid)

      if (x,y,dir) in visited:
        part_two += 1
        #print( visited )
        #print( x,y,dir )
        #display(grid, (i, j))
        print( "   LOOP!", i, j, part_two)
        break
      else:
        visited.add( (x,y,dir) )
        #grid[y][x] = 10 + dir

    grid[j][i] = 0

print( part_two )

