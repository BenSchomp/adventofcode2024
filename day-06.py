grid = []
EMPTY = -1
BLOCK = -2
dirs = [(0,-1), (1,0), (0,1), (-1,0)] # N, E, S, W

file = open('day-06.txt', 'r')
curRow = 0
for line in file:
  row = []

  curCol = 0
  for c in line.strip():
    if c == '.':
      row.append(EMPTY)
    elif c == '#':
      row.append(BLOCK)
    elif c == '^':
      (startX, startY) = (curCol, curRow)
      row.append(EMPTY)

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
dir = 0 # (0: N, 1: E, 2: S, 3: W)

while True:
  (dx, dy) = dirs[dir]
  x += dx
  y += dy

  if x < 0 or x >= width or y < 0 or y >= height:
    break

  if grid[y][x] == BLOCK:
    dir = (dir+1)%4
    x -= dx
    y -= dy
  else:
    visited.add( (x,y) )

print( len(visited) )

# --- PART TWO ---

part_two = 0
path = visited

for (i, j) in path:
  if grid[j][i] == BLOCK:
    continue
  else:
    grid[j][i] = BLOCK

  (x, y) = (startX, startY)
  dir = 0
  visited = set()
  visited.add( (x,y,dir) )

  while True:
    (dx, dy) = dirs[dir]
    x += dx
    y += dy

    if x < 0 or x >= width or y < 0 or y >= height:
      break

    if grid[y][x] == BLOCK:
      dir = (dir+1)%4
      x -= dx
      y -= dy

    if (x,y,dir) in visited:
      part_two += 1
      break
    else:
      visited.add( (x,y,dir) )

  grid[j][i] = EMPTY

print( part_two )

