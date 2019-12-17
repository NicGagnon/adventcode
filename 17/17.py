from collections import deque

def fill_command(command, length):
  if len(str(command)) != length:
    return str(command).zfill(length)
  else:
    return str(command)


def param_value(x, index, opcode, offset, base_mem):
  if opcode == '0':
    create_index(x, x[index + offset])
    return x[x[index + offset]]
  elif opcode == '1':
    return x[index + offset]
  else:
    create_index(x, base_mem + x[index + offset])
    return x[base_mem + x[index + offset]]


def addr_value(x, index, opcode, offset, base_mem):
  if opcode == '0':
    create_index(x, x[index + offset])
    return x[index + offset]
  elif opcode == '1':
    return index + offset
  else:
    create_index(x, base_mem + x[index + offset])
    return base_mem + x[index + offset]


def create_index(x, value):
  if value not in x:
    x[value] = 0


def add_available_tiles(Q, R, dx, dy, dz, grid):
  if (dx, dy + 1) not in grid:
    Q.insert(0, (1, dx, dy+1, dz))
  elif grid[(dx, dy + 1)] > -1:
    R.insert(0, (1, dx, dy + 1, dz-1))
  if (dx, dy - 1) not in grid:
    Q.insert(0, (2, dx, dy-1, dz))
  elif grid[(dx, dy - 1)] > -1:
    R.insert(0, (2, dx, dy - 1, dz-1))
  if (dx - 1, dy) not in grid:
    Q.insert(0, (3, dx-1, dy, dz))
  elif grid[(dx-1, dy)] > -1:
    R.insert(0, (3, dx-1, dy, dz-1))
  if (dx + 1, dy) not in grid:
    Q.insert(0, (4, dx+1, dy, dz))
  elif grid[(dx + 1, dy)] > -1:
    R.insert(0, (4, dx + 1, dy, dz-1))


def Q_tiles(Q, dx, dy, dz, grid):
  if (dx, dy + 1) not in grid:
    Q.insert(0, (1, dx, dy+1, dz))
  if (dx, dy - 1) not in grid:
    Q.insert(0, (2, dx, dy-1, dz))
  if (dx - 1, dy) not in grid:
    Q.insert(0, (3, dx-1, dy, dz))
  if (dx + 1, dy) not in grid:
    Q.insert(0, (4, dx+1, dy, dz))

def print_grid(g):
  for i in range(-13, 10):
    for j in range(-11, 8):
      if (j, i) in g:
        if (g[(j, i)] == -1):
          print("|", end="")
        else:
          print("O", end="")
      else:
        print("-", end="")
    print()


def thruster_calculation(x, y):
  mem, index = 0, 0
  game_index, grid = 0, {}
  dx, dy, dz = 0, 0, 1
  scaffold = []
  while x[index] != 99:
    command = x[index]
    instruction = [int(d) for d in str(command)][-1]

    if instruction == 1 or instruction == 2:
      # Read Opcode
      opcodeC, opcodeB, opcodeA = fill_command(command, 5)[:3]
      first_value = param_value(x, index, opcodeA, 1, mem)
      second_value = param_value(x, index, opcodeB, 2, mem)
      third_value = addr_value(x, index, opcodeC, 3, mem)

      # Read Instructions
      if instruction == 1:
        x[third_value] = first_value + second_value
      else:
        x[third_value] = first_value * second_value

      index += 4
    elif instruction == 3 or instruction == 4:
      opcode = fill_command(command, 3)[0]
      if instruction == 3:
        # user_ID = input("Please input user ID of the system you wish to test: ")

        if opcode == '0':
          x[x[index + 1]] = 1
        else:
          x[mem + x[index + 1]] = 1
      else:  # instruction 4
        scaffold.append(param_value(x, index, opcode, 1, mem))

        # print(param_value(x, index, opcode, 1, mem))
      index += 2
    elif instruction == 5 or instruction == 6:
      opcodeB, opcodeA = fill_command(command, 4)[:2]
      first_value = param_value(x, index, opcodeA, 1, mem)
      second_value = param_value(x, index, opcodeB, 2, mem)
      if instruction == 5:
        if first_value != 0:
          index = second_value
        else:
          index += 3
      else:  # instruction 6
        if first_value == 0:
          index = second_value
        else:
          index += 3
    elif instruction == 7 or instruction == 8:
      opcodeC, opcodeB, opcodeA = fill_command(command, 5)[:3]
      first_value = param_value(x, index, opcodeA, 1, mem)
      second_value = param_value(x, index, opcodeB, 2, mem)
      third_value = addr_value(x, index, opcodeC, 3, mem)
      create_index(x, x[index + 3])
      if instruction == 7:
        x[third_value] = 1 if first_value < second_value else 0
      else:
        x[third_value] = 1 if first_value == second_value else 0
      index += 4
    elif instruction == 9:
      opcode = fill_command(command, 3)[0]
      mem += param_value(x, index, opcode, 1, mem)
      index += 2
    else:
      raise ValueError("unknown instruction")
  return scaffold



def has_neighbors(i, j, s):
  neighbors = [0, 0]
  code = i*42+j
  if 42 <= code <= len(s)-42:
    if s[code-1] == 35 and s[code+1] == 35:
      neighbors[0] = 1
    if s[code-42] == 35 and s[code+42] == 35:
      neighbors[1] = 1
  return sum(neighbors) > 1


if __name__ == '__main__':
  A = open('17.in').read().split(',')
  B = {}
  for i, x in enumerate(A):
    B[i] = int(x)
  sca = thruster_calculation(B, 1)
  for index, code in enumerate(sca):
    if code == 46:
      print(".", end="")
    elif code == 35:
      print("#", end="")
    elif code == 94:
      print("<", end="")
    else:
      print()
  intersection = 0
  for x in range(47):
    for y in range(42):
      code = x*42+y
      if sca[code] == 35:
        if has_neighbors(x, y, sca):
          intersection += x * y
  print(intersection)
