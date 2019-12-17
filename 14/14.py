from collections import deque
from math import ceil


A = open('14.in').read().split('\n')[:-1]
B = {}
C = {}
start = 'ORE'
for i, r in enumerate(A):
  B[r.split()[-1]] = r.split('=>')[0]
  C[r.split()[-1]] = int(r.split()[-2])

D = {}
Q = deque()
Q.append(('FUEL', 3279311))
t = 0

while Q:
  x, d = Q.popleft()
  for y in B[x].split(','):
    m, i, j = 0, 0, 0
    y0, y1 = y.strip().split()
    y0 = int(y0) * d
    if y1 == 'ORE':
      t += y0
      continue

    if y1 in D:
      i, j = D[y1]

    m = ceil((y0 + j) / C[y1]) - i


    D[y1] = [m+i, y0+j]
    Q.append((y1, m))
print(t)

