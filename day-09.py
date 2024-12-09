def checksum( d ):
  chksum = 0
  for i in range(len(d)):
    if d[i] != EMPTY:
      chksum += (i * d[i])
  return chksum

def compact( d ):
  max_i = len(d)
  i = 0
  j = max_i-1
  count = 0

  while True:
    found_i = found_j = False

    while i < max_i:
      if d[i] == EMPTY:
        found_i = True
        break
      i += 1

    while j >= 0:
      if d[j] != EMPTY:
        found_j = True
        break
      j -= 1

    if found_i and found_j:
      d[i] = d[j]
      count += 1
    else:
      del d[max_i-count:]
      break

    i += 1
    j -= 1

  return checksum(d)

def compact2( d, sizes, empties ):
  for file_id in range( len(sizes)-1, -1, -1 ):
    (size, file_idx) = sizes[file_id]

    empty_indicies = sorted(empties.keys())
    for empty_idx in empty_indicies:
      if empty_idx >= file_idx:
        break

      if empties[empty_idx] >= size:
        for offset in range(size):
          d[empty_idx+offset] = file_id
          d[file_idx+offset] = EMPTY

        empties[empty_idx+size] = empties[empty_idx]-size
        del empties[empty_idx]
        break

  return checksum(d)

# --- main ---

EMPTY = -1
disk = []
file_sizes = []
empty_blocks = {}

file = open('day-09.txt', 'r')
for line in file:
  line = line.strip()

  id = i = 0
  for c in range(len(line)):
    size = int(line[c])
    if c == id*2: # file
      disk += [id]*size
      file_sizes.append( (size, i))
      id += 1

    else: # space
      disk += ( [EMPTY]*size )
      if size > 0:
        empty_blocks[i] = size

    i += size

file.close

disk2 = disk.copy()
part_one = compact( disk )
print( part_one )

part_two = compact2( disk2, file_sizes, empty_blocks )
print( part_two )
