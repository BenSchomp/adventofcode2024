def solve( r, v ):
  # this is recursive
  n = len(v)

  if n == 2:
    if v[0] + v[1] == r:
      print( '  GOOD:', v[0], '+', v[1], '=', r )
      return True
    elif v[0] * v[1] == r:
      print( '  GOOD:', v[0], '*', v[1], '=', r )
      return True
    else:
      return False

  else:
    result = solve( r, [v[0]+v[1]] + v[2:] )
    if result:
      return True
    else:
      return solve( r, [v[0]*v[1]] + v[2:] )

# --- main ---
part_one = 0
file = open('day-07.txt', 'r')

for line in file:
  if not line.strip():
    exit()
  (left, right) = line.strip().split(':')
  result = int(left)
  values = [int(x) for x in right.split()]

  print( result, values )
  if solve( result, values ):
    part_one += result
file.close()

print( part_one )