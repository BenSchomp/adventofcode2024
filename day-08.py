
file = open('day-08.txt', 'r')

antennas = {}
antinodes = set()

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

#print( width, height )

# now calculate anitnodes for each antenna
for k, v in antennas.items():
  #print( k, v )

  num_pairs = len(v)
  for i in range(num_pairs):
    for j in range(i+1, num_pairs):

      #print( i, j )

      dx = v[i][0] - v[j][0]
      dy = v[i][1] - v[j][1]
      #print( dx, dy )

      newX = v[i][0] + dx
      newY = v[i][1] + dy
      if newX >= 0 and newX < width and newY >= 0 and newY < height:
        antinodes.add( (newX, newY) )
        #print( '  ', newX, newY)

      newX = v[j][0] - dx
      newY = v[j][1] - dy
      if newX >= 0 and newX < width and newY >= 0 and newY < height:
        antinodes.add( (newX, newY) )
        #print( '  ', newX, newY)

#print( antennas )
#print( antinodes )
part_one = len(antinodes)
print( part_one )

