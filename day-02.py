file = open('day-02.txt', 'r')


def isSafe(row):
  direction = None
  prev = row[0]

  #print( row )
  for r in row[1:]:
    delta = r - prev
    #print( r, prev, delta, direction )
    if delta == 0 or abs(delta) > 3:
      #print( 'FAIL, delta:', delta )
      return False

    if not direction:
      direction = delta / abs(delta)
    else:
      if direction != delta / abs(delta):
        #print( 'FAIL, direction:', direction )
        return False

    prev = r

  #print( 'safe!' )
  return True

part_one = 0
for line in file:
  line = [int(x) for x in line.strip().split()]

  if isSafe(line):
    part_one += 1

file.close()

print( part_one )
