# layer is 25 by 6 so 150 pixels
# 0 is black, 1 is white, and 2 is transparent

A = open('8.in').read()
n = 150
layer_n = [A[i:i+n] for i in range(0, len(A), n)][:-1]
fewest_zeros, target_layer, = float('inf'), -1
for index, layer in enumerate(layer_n):
  if layer.count('0') < fewest_zeros:
    fewest_zeros, target_layer = layer.count('0'), index

final_layer = '2' * 150
for layer in layer_n:
  for index, pixel in enumerate(layer):
    if int(pixel) < int(final_layer[index]) == 2:
      final_layer = final_layer[:index] + pixel + final_layer[index+1:]

for i in range(0, 150, 25):
  print(final_layer[i:i+25])

