# concatenate 2 ints (returns an int)
def concat( a, b ):
  return int( str(a) + str(b) )

# this is a recursive function
# r: the result to look for
# t: the terms (a list)
# p2:  if True, use "part two" logic
def solve( r, t, p2=False ):
  # base case: only 2 terms, try all the operators and see if we get a match
  if len(t) == 2:
    return (t[0] + t[1] == r) or \
           (t[0] * t[1] == r) or \
           (p2 and (concat(t[0], t[1]) == r))

  # else recurse, iterating through the operators on the 1st two terms
  else:
    return solve(r, [t[0]+t[1]] + t[2:], p2 ) or \
           solve( r, [t[0]*t[1]] + t[2:], p2 ) or \
           (p2 and solve( r, [concat(t[0], t[1])] + t[2:], p2 ) )

# --- main ---
part_one = part_two = 0
file = open('day-07.txt', 'r')

for line in file:
  if not line.strip():
    exit()
  (left, right) = line.strip().split(':')
  result = int(left)
  terms = [int(x) for x in right.split()]

  if solve( result, terms ):
    part_one += result

  if solve( result, terms, True ):
    part_two += result

file.close()

print( part_one )
print( part_two )
