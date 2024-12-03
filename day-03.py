import re

memory = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'

part_one = 0

file = open('day-03.txt', 'r')
for line in file:
  instructions = re.findall('mul\(\d{1,3},\d{1,3}\)', line)

  print( instructions )

  for i in instructions:
    (f1, f2) = i.split('(')[1][:-1].split(',')
    part_one += (int(f1) * int(f2))

print( part_one )

