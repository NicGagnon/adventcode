

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


def thruster_calculation(x, i):
  mem, index = 0, 0
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
          x[x[index + 1]] = i
        else:
          x[mem + x[index + 1]] = i
      else:  # instruction 4
        print(param_value(x, index, opcode, 1, mem))
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


if __name__ == '__main__':
  A = open('9.in').read().split(',')
  B = {}
  for i, x in enumerate(A):
    B[i] = int(x)
  thruster_calculation(B, 2)

