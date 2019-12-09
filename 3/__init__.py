import pandas as pd

def read_command(c, x, y):
  """
  Calculate the directional vector from a command
  :param x: string command
  :return: the vector value of latitude and longitude for the command
  """
  direction = c[0]
  if direction == "L":
    return -1*int(c[1:]) + x, y, [",".join([str(-1*index + x), str(y)]) for index in range(0, (int(c[1:])+1))]
  elif direction == "R":
    return int(c[1:]) + x, y, [",".join([str(index + x), str(y)]) for index in range(0, (int(c[1:])+1))]
  elif direction == "U":
    return x, int(c[1:]) + y, [",".join([str(x), str(index + y)]) for index in range(0, (int(c[1:])+1))]
  elif direction == "D":
    return x, -1 * int(c[1:]) + y, [",".join([str(x), str(-1*index + y)]) for index in range(0, (int(c[1:])+1))]
  else:
    raise ValueError("Invalid Direction")


def read_command_distance(c, x, y):
  """
  Calculate the directional vector from a command
  :param x: string command
  :return: the vector value of latitude and longitude for the command
  """
  direction = c[0]
  value = int(c[1:])
  if direction == "L":
    return -1*value + x, y, value, [",".join([str(-1*index + x), str(y)]) for index in range(0, (value+1))]
  elif direction == "R":
    return value + x, y, value, [",".join([str(index + x), str(y)]) for index in range(0, (value+1))]
  elif direction == "U":
    return x, value + y, value, [",".join([str(x), str(index + y)]) for index in range(0, (value+1))]
  elif direction == "D":
    return x, -1 * value + y, value, [",".join([str(x), str(-1*index + y)]) for index in range(0, (value+1))]
  else:
    raise ValueError("Invalid Direction")


def create_coordinate_list(w):
  """
  Calculate Manhanttan distance for a set of coordinates
  :param w: coordinate list
  :return: manhanttan distance
  """
  x, y, coordinate_list = 0, 0, []
  for command in w:
    x, y, coords = read_command(command, x, y)
    coordinate_list.extend(coords)
  return coordinate_list


def find_distance_to_wire(i, w):
  x, y, dist_so_far = 0, 0, 0,
  for command in w:
    x, y, dist, coords = read_command_distance(command, x, y)
    if i in coords:
      return dist_so_far + coords.index(i)
    else:
      dist_so_far += dist
  return -1


if __name__ == '__main__':
  df = pd.read_csv('input.csv', header=None)
  coordinates = []
  for wire in df.itertuples(index=False):
    coordinates.append(create_coordinate_list(wire))

  intersection = [list(set(coordinates[index-1]) & set(coordinates[index])) for index in range(1, len(coordinates))]
  intersection = intersection[len(intersection)-1]

  path_distance = []
  for i in intersection:
    total_distance = 0
    for wire in df.itertuples(index=False):
      total_distance += find_distance_to_wire(i, wire)
    path_distance.append(total_distance)
  path_distance = sorted(path_distance)
  print("the shortest path is {}".format(path_distance[1]))


  """
  # For part A
  closest_distance = float('inf')
  for coord in intersection:
    new_distance = find_distance(coord)
    if 0 < new_distance < closest_distance:
      closest_distance = new_distance
  print("closest distance is {}".format(closest_distance))
  """

