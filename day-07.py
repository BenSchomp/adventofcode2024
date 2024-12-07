# concatenate 2 ints (returns an int)
def concat( a, b ):
  return int( str(a) + str(b) )

# this is recursive (if part two, call w p2 as True)
def solve( r, v, p2=False ):
  # base case: 2 values, try all the operators and see if we get a match
  if len(v) == 2:
    if v[0] + v[1] == r:
      return True
    elif v[0] * v[1] == r:
      return True
    elif p2 and concat(v[0], v[1]) == r:
      return True
    else:
      return False

  # else recurse, iterating through the operators on the 1st two values
  else:
    result = solve( r, [v[0]+v[1]] + v[2:], p2 )
    if result:
      return True

    result = solve( r, [v[0]*v[1]] + v[2:], p2 )
    if result:
      return True

    if p2:
      return solve( r, [concat(v[0], v[1])] + v[2:], p2 )
    else:
      return False

# --- main ---
part_one = part_two = 0
file = open('day-07.txt', 'r')

for line in file:
  if not line.strip():
    exit()
  (left, right) = line.strip().split(':')
  result = int(left)
  values = [int(x) for x in right.split()]

  if solve( result, values ):
    part_one += result

  if solve( result, values, True ):
    part_two += result

file.close()

print( part_one )
print( part_two )
