
file = open('day-08.txt', 'r')

antennas = {}
part_one = set()
part_two = set()

width = height = None

y = 0
for line in file:
  line = line.strip()

  x = 0
  for c in line:
    if c != '.':
      if not c in antennas:
        antennas[c] = []
      antennas[c].append( (x,y) )

    x += 1
  if not width:
    width = x
  y += 1
height = y
file.close()

# now calculate anitnodes for each antenna
for k, v in antennas.items():
  num_pairs = len(v)
  for i in range(num_pairs):
    for j in range(i+1, num_pairs):
      x1 = v[i][0]
      y1 = v[i][1]
      part_two.add( (x1, y1) )

      x2 = v[j][0]
      y2 = v[j][1]
      part_two.add( (x2, y2) )

      dx = x2 - x1
      dy = y2 - y1

      once = False
      newX = x1 - dx
      newY = y1 - dy
      while newX >= 0 and newX < width and newY >= 0 and newY < height:
        if not once:
          part_one.add( (newX, newY) )
          once = True
        part_two.add( (newX, newY) )

        newX -= dx
        newY -= dy

      once = False
      newX = x2 + dx
      newY = y2 + dy
      while newX >= 0 and newX < width and newY >= 0 and newY < height:
        if not once:
          part_one.add( (newX, newY) )
          once = True
        part_two.add( (newX, newY) )

        newX += dx
        newY += dy

print( len(part_one) )
print( len(part_two) )

