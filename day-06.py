
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
      (x, y) = (curCol, curRow)
      row.append(0)

    curCol += 1

  grid.append(row)
  curRow += 1

file.close()

width = curCol
height = curRow

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




