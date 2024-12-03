import re

def decrypt(memory):
  result = 0
  instructions = re.findall(r'mul\(\d{1,3},\d{1,3}\)', memory)

  for i in instructions:
    (f1, f2) = i.split('(')[1][:-1].split(',')
    result += (int(f1) * int(f2))

  return result

def decrypt2(memory):
  global enabled
  result = 0
  instructions = re.findall(r'(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))', memory)

  for i in instructions:
    if i == "do()":
      enabled = True
    elif i == "don't()":
      enabled = False;
    elif i[:3] == "mul" and enabled:
      (f1, f2) = i.split('(')[1][:-1].split(',')
      result += (int(f1) * int(f2))

  return result

# --- main ---

enabled = True
part_one = part_two = 0

file = open('day-03.txt', 'r')
for line in file:
  part_one += decrypt(line)
  part_two += decrypt2(line)

file.close()

print( part_one )
print( part_two )
