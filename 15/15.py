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


def add_available_tiles(Q, dx, dy, dz, grid):
  if (dx, dy + 1) not in grid:
    Q.insert(0, (dx, dy+1, dz, 1))
  if (dx, dy - 1) not in grid:
    Q.insert(0, (dx, dy-1, dz, 2))
  if (dx - 1, dy) not in grid:
    Q.insert(0, (dx-1, dy, dz, 3))
  if (dx + 1, dy) not in grid:
    Q.insert(0, (dx+1, dy, dz, 4))


def reverse(x, dx, dy, dz):
  if x == 1:
    return dx, dy-1, dz-1, 2
  elif x == 2:
    return dx, dy+1, dz-1, 1
  elif x == 3:
    return dx+1, dy, dz-1, 4
  else:
    return dx-1, dy, dz-1, 3


def prior_location(x, dx, dy):
  if x == 1:
    return dx, dy-1
  elif x == 2:
    return dx, dy+1
  elif x == 3:
    return dx+1, dy
  else:
    return dx-1, dy


def print_grid(g):
  for i in range(-21, 21):
    for j in range(-21, 21):
      if (j, i) in g:
        if (g[(j, i)] == -1):
          print("|", end="")
        else:
          print("O", end="")
      else:
        print("-", end="")
    print()


def thruster_calculation(x):
  mem, index, grid = 0, 0, {(0, 0): -1}
  dx, dy, dz = 0, 0, 0
  Q = deque()
  first_flag = True
  add_available_tiles(Q, dx, dy, dz + 1, grid)
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
        if Q:
          dx, dy, dz, direction = Q.popleft()
        else:
          print(max(grid.values()))
          print_grid(grid)
          exit(1)
        if opcode == '0':
          x[x[index + 1]] = direction
        else:
          x[mem + x[index + 1]] = direction
      else:  # instruction 4
        status_code = param_value(x, index, opcode, 1, mem)
        if status_code == 0:
          grid[(dx, dy)] = -1
        elif status_code == 1:
          px, py = prior_location(direction, dx, dy)
          if dz > grid[(px, py)]:
            grid[(dx, dy)] = dz
            Q.insert(0, (reverse(direction, dx, dy, dz)))
            add_available_tiles(Q, dx, dy, dz+1, grid)
        elif status_code == 2:
          if first_flag:
            grid = {(0, 0): 0}
            Q.clear()
            add_available_tiles(Q, 0, 0, 1, grid)
            first_flag = False
          else:
            print(max(grid.values()))
            exit(1)

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
  return grid




if __name__ == '__main__':
  A = open('15.in').read().split(',')
  B = {}
  for i, x in enumerate(A):
    B[i] = int(x)
  print(thruster_calculation(B))

