from math import gcd
A = open('10.in').read().split('\n')
asteroids = []
poop = {}


def optimal_coord(x, y):
  if x == 0:
    return 0, -1 if y < 0 else 1
  elif y == 0:
    return -1 if x < 0 else 1, 0
  else:
    g = gcd(x, y)
    return x / g, y / g


for i, row in enumerate(A):
  for j, char in enumerate(row):
    if char == '#':
      asteroids.append((j, i))


for i, coordinates in enumerate(asteroids):
  oa = [x for index, x in enumerate(asteroids) if index != i]
  poop[coordinates] = []
  for o in oa:
    xvalue = o[0] - coordinates[0]
    yvalue = o[1] - coordinates[1]
    poop[coordinates].append(optimal_coord(xvalue, yvalue))

for key in poop:
  poop[key] = set(poop[key])


print(max([len(x) for x in poop.values()]))
for key in poop:
  if len(poop[key]) == 286:
    print(key)
target = poop[(22, 25)]
target = [(x+22, y+25) for x, y in target]
slopes = {}
for i in range(25):
  for j in range(22):
    if (j, i) in target:
      slopes[(j,i)] = (25-i)/(j-22)
print(len(slopes))
print(sorted(slopes.values()))
ss = sorted(slopes.values())
print(ss[86])
for s in slopes:
  if slopes[s] == -1.2352941176470589:
    print(s)

