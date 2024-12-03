import re

def execute(memory, part):
  global enabled
  result = 0

  if part == 1:
    instructions = re.findall(r'mul\(\d{1,3},\d{1,3}\)', memory)
  else:
    instructions = re.findall(r'(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))', memory)

  for i in instructions:
    if i == "do()":
      enabled = True
    elif i == "don't()":
      enabled = False;
    elif (part == 1 or enabled) and i[:3] == "mul":
      (f1, f2) = i.split('(')[1][:-1].split(',')
      result += (int(f1) * int(f2))

  return result

# --- main ---

enabled = True
part_one = part_two = 0

file = open('day-03.txt', 'r')
for line in file:
  part_one += execute(line, 1)
  part_two += execute(line, 2)

file.close()

print( part_one )
print( part_two )
