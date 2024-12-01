file = open('day-01.txt', 'r')

left = []
right = []
right_counts = {}

for line in file:
  line = line.strip()
  (l, r) = line.split()
  left.append(int(l))
  right.append(int(r))

  needle = int(r)
  if needle in right_counts:
    right_counts[needle] += 1
  else:
    right_counts[needle] = 1
file.close()

left.sort()
right.sort()

part_one = part_two = 0
for i in range(len(left)):
  part_one += abs(left[i] - right[i])

  if left[i] in right_counts:
    part_two += left[i] * right_counts[left[i]]

print( part_one )
print( part_two )
