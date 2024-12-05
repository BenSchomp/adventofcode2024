

def fix( u ):
  # check each neighboring pair for order
  # a "buble sort" of sorts
  done = False
  while not done:
    swaps = 0
    for i in range(len(u)-1):
      if u[i] in rules:
        if u[i+1] in rules[u[i]]:
          continue # neighbors are in order

      if u[i+1] in rules:
        if u[i] in rules[u[i+1]]:
          # neighbors out of order, swap them!
          tmp = u[i]
          u[i] = u[i+1]
          u[i+1] = tmp
          swaps += 1

    if swaps == 0:
      done = True

  return u

# --- main ---
rules = {}
updates = []
parsing_rules = True

file = open('day-05.txt', 'r')
for line in file:
  line = line.strip()
  if not line:
    parsing_rules = False
    continue

  if parsing_rules:
    (a, b) = [int(x) for x in line.split("|")]
    if a not in rules:
      rules[a] = set()
    rules[a].add(b)
  else:
    update = [int(x) for x in line.split(",")]
    updates.append(update)

file.close()

part_one = part_two = 0
for update in updates:
  fail = False

  p = 0
  for page in update:
    if page in rules:
      rule = rules[page]

      for r in rule:
        if r not in update:
          continue

        i = update.index(r)
        if p > i:
          fail = True # fail
          break

    if fail:
      break
    p += 1

  mid = int(len(update)/2)
  if fail:
    part_two += fix(update)[mid]
  else:
    part_one += update[mid]

print( part_one )
print( part_two )

