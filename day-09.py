EMPTY = -1

def display(d):
  for c in d:
    if c == EMPTY:
      print( '.', end='' )
    else:
      print( c, end='' )
  print()

def compact(d):
  max_i = len(d)
  i = 0
  j = max_i-1
  count = 0

  while True:
    left = right = False

    while i < max_i:
      if d[i] == EMPTY:
        left = True
        break
      i += 1

    while j >= 0:
      if d[j] != EMPTY:
        right = True
        break
      j -= 1

    if left and right:
      d[i] = d[j]
      count += 1
    else:
      del d[max_i-count:]
      break

    i += 1
    j -= 1

  chksum = 0
  for i in range(len(d)):
    chksum += (i * d[i])
  return chksum

# --- main ---

file = open('day-09.txt', 'r')

disk = []
for line in file:
  line = line.strip()

  id = 0
  for c in range(len(line)):
    if c == id*2: # file
      disk += [id]*int(line[c])
      id += 1
    else: # space
      disk += ( [EMPTY]*int(line[c]) )

file.close

display( disk )
part_one = compact( disk )
display( disk )

print( part_one )
