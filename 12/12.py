from operator import add


def comp(i, j):
  change = 0
  for k in j:
    if i < k:
      change += 1
    elif i > k:
      change -= 1
  return change


def calculate_gravity(moons_p, moons_v):
  for moon in moons_p:
    x, y, z = moons_p[moon]
    x1, y1, z1 = zip(*moons_p.values())
    x = comp(x, x1)
    # y = comp(y, y1)
    # z = comp(z, z1)
    # moons_v[moon] = list(map(add, moons_v[moon], [x, y, z]))
    moons_v[moon][0] = moons_v[moon][0] + x


def calculate_position(moons_p, moons_v):
  for moon in moons_p:
    moons_p[moon] = list(map(add, moons_p[moon], moons_v[moon]))


def original_position(moons_p, moons_v, ap):
  super_position = []
  for moon in moons_p:
    super_position.append(moons_p[moon][0])
    super_position.append(moons_v[moon][0])
  super_position = tuple(super_position)
  if super_position in ap:
    return True
  else:
    ap[super_position] = True
    return False


def calculate_energy(moons_p, moons_v):
  te, pe, ke = 0, 0, 0
  for moon in moons_p:
    pe = sum([abs(x) for x in moons_p[moon]])
    ke = sum([abs(x) for x in moons_v[moon]])
    te += pe * ke
  return te


if __name__ == '__main__':

  A = open('12.in').read().split('\n')[:-1]
  all_positions = {}
  moons_p = {}
  moons_v = {}
  step = 0
  og = False

  for index, moon in enumerate(A):
    x, y, z = moon.split(',')
    x = int(x[3:])
    y = int(y[3:])
    z = int(z[3:-1])
    moons_p[index] = [x, y, z]
    moons_v[index] = [0, 0, 0]

  while not og:
    calculate_gravity(moons_p, moons_v)
    calculate_position(moons_p, moons_v)
    step += 1
    if original_position(moons_p, moons_v, all_positions):
      print(step)

  # total_e = calculate_energy(moons_p, moons_v)
  print(step)
