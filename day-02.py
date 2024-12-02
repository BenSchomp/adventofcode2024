def isSafe(row):
  direction = None
  prev = row[0]

  for r in row[1:]:
    delta = r - prev
    if delta == 0 or abs(delta) > 3:
      return False

    if not direction:
      direction = delta / abs(delta)
    elif direction != delta / abs(delta):
      return False

    prev = r

  return True

def isDampenerSafe(row):
  for i in range(len(row)):
    test = row[:i] + row[i+1:]
    if isSafe(test):
      return True

  return False

# --- main ---

file = open('day-02.txt', 'r')

part_one = part_two = 0
for line in file:
  line = [int(x) for x in line.strip().split()]

  if isSafe(line):
    part_one += 1
    part_two += 1

  elif isDampenerSafe(line):
    part_two += 1

file.close()

print( part_one )
print( part_two )
