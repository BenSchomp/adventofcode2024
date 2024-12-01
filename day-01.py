file = open('day-01.txt', 'r')

left = []
right = []
for line in file:
  line = line.strip()
  (l, r) = line.split()
  left.append(int(l))
  right.append(int(r))
file.close()

left.sort()
right.sort()

part_one = 0
for i in range(len(left)):
  part_one += abs(left[i] - right[i])

print( part_one )


