def checksum(d):
  chksum = 0
  for i in range(len(d)):
    if d[i] != EMPTY:
      chksum += (i * d[i])
  return chksum

def compact(d):
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

def compact2( d, s, e ):
  max_i = len(d)
  for file_id in range(len(s)-1, -1, -1):
    size = s[file_id][0]
    file_idx = s[file_id][1]

    empty_indicies = sorted(e.keys())
    for empty_idx in empty_indicies:
      if empty_idx >= file_idx:
        break

      if e[empty_idx] >= size:
        for offset in range(size):
          d[empty_idx+offset] = file_id
          d[file_idx+offset] = EMPTY

        e[empty_idx+size] = e[empty_idx]-size
        del e[empty_idx]
        break

  return checksum(d)

# --- main ---

EMPTY = -1
disk = []
sizes = []
empties = {}

file = open('day-09.txt', 'r')
for line in file:
  line = line.strip()

  id = i = 0
  for c in range(len(line)):
    size = int(line[c])
    if c == id*2: # file
      disk += [id]*size
      sizes.append( (size, i))
      id += 1

    else: # space
      disk += ( [EMPTY]*size )
      if size > 0:
        empties[i] = size

    i += size

file.close
disk2 = disk.copy()

part_one = compact( disk )
print( part_one )

part_two = compact2( disk2, sizes, empties )
print( part_two )
