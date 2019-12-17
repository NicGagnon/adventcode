from math import ceil
from itertools import cycle, accumulate

s = open("16.in").read()[:-1]
offset = int(s[:7])
digits = [int(i) for i in s]
# If `rep` is `digits` repeated 10K times, construct:
#     arr = [rep[-1], rep[-2], ..., rep[offset]]
l = 10000 * len(digits) - offset
r = len(digits)
i = cycle(reversed(digits))
arr = [next(i) for _ in range(l)]
# Repeatedly take the partial sums mod 10
for _ in range(100):
    arr = [n % 10 for n in accumulate(arr)]
print("".join(str(i) for i in arr[-1:-9:-1]))


"""A = open("16.in").read()[:-1]
#A = A * 10000
default_repeat = [0,1,0,-1]
phase = 100

for i in range(phase):
  B = ''
  for x in range(len(A)):
    pattern = [val for val in default_repeat for _ in range(x + 1)] if x > 0 else default_repeat.copy()
    pattern.append(pattern.pop(0))
    signal = [int(val) for val in A]
    pattern *= ceil(len(signal) / len(pattern))
    h = sum([a*b for a,b in zip(pattern, signal)])
    B += str(h)[-1]
  A = B
print(A)
"""

