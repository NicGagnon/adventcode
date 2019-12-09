import pandas as pd

class Orbit:
  def __init__(self, value):
    self.o = None
    self.ob = []
    self.value = value
  def orbiting(self, obj):
    self.o = obj
  def orbited_by(self, obj):
    self.ob.append(obj)
  def orbit_value(self):
    return self.value
  def contains(self, target):
    if self.value == target.value:
      return 1
    else:
      total = 0
      for children in self.ob:
        total += children.contains(target)
      return total


def indirect_orbits(obj, orbits):
  if obj not in orbits:
    return 0
  else:
    ind_count = 0
    for i in orbits[obj]:
      ind_count += 1 + indirect_orbits(i, orbits)
    return ind_count


def find_orbit(name, orbits):
  for orbit in orbits:
    if name == orbit.value:
      return orbit
  return None


def create_orbit(name, orbits):
  for orbit in orbits:
    if name == orbit.value:
      return orbit
  return Orbit(name)


def add_orbit(name, orbit_names, O, orbits):
  if name not in orbit_names:
    orbits.append(O)
    orbit_names.append(name)


def relationship_length(root, target, seen):
  if root.value == target.value:
    return -1
  elif root.contains(target) > 0:
    for children in root.ob:
      if children.contains(target) > 0:
        return 1 + relationship_length(children, target, seen)
  else:
    seen.append(root)
    root = root.o
    return 1 + relationship_length(root, target, seen)


if __name__ == '__main__':
  df = pd.read_csv('7.csv', header=None)
  orbits, orbit_names, checksum = [], [], 0
  for row in df.itertuples():
    A, B = row[1].split(')')
    OA, OB = create_orbit(A, orbits), create_orbit(B, orbits)
    OA.orbited_by(OB)
    OB.orbiting(OA)
    add_orbit(A, orbit_names, OA, orbits)
    add_orbit(B, orbit_names, OB, orbits)

  my_orbit = find_orbit('YOU', orbits)
  santa_orbit = find_orbit('SAN', orbits)
  assert my_orbit
  assert santa_orbit


  """
  # Checks all the direct + indirect orbits
  for i in orbits:
    checksum += indirect_orbits(i, orbits)
  print("checksum sum is {}".format(checksum))
  """

  # Shortest orbit path to Santa
  shortest_path = relationship_length(my_orbit, santa_orbit, [])
  print("Shortest number of Orbit hops is {}".format(shortest_path-1))
