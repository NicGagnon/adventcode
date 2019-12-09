import pandas as pd
from itertools import permutations



def fill_command(command, length):
  if len(str(command)) != length:
    return str(command).zfill(length)
  else:
    return str(command)


def first_param_value(df, index, opcode, offset):
  if opcode == '0':
    return df.iloc[0, df.iloc[0, index + offset]]
  else:
    return df.iloc[0, index + offset]


def thruster_calculation(i, j):
  df = pd.read_csv('7.csv', header=None)
  amplifier_output, index = -1, 0
  i_flag = False
  while df.iloc[0, index] != 99:
    command = df.iloc[0, index]
    instruction = [int(d) for d in str(command)][-1]

    if instruction == 1 or instruction == 2:
      # Read Opcode
      opcodeB, opcodeA = fill_command(command, 4)[:2]
      first_value = first_param_value(df, index, opcodeA, 1)
      second_value = first_param_value(df, index, opcodeB, 2)

      # Read Instructions
      if instruction == 1:
        df.iloc[0, df.iloc[0, index + 3]] = first_value + second_value
      else:
        df.iloc[0, df.iloc[0, index + 3]] = first_value * second_value

      index += 4
    elif instruction == 3 or instruction == 4:
      opcode = fill_command(command, 3)[0]
      if instruction == 3:
        # user_ID = input("Please input user ID of the system you wish to test: ")
        if i_flag:
          df.iloc[0, df.iloc[0, index + 1]] = j
        else:
          df.iloc[0, df.iloc[0, index + 1]] = i
          i_flag = True
      else:  # instruction 4
        amplifier_output = first_param_value(df, index, opcode, 1)
      index += 2
    elif instruction == 5 or instruction == 6:
      opcodeB, opcodeA = fill_command(command, 4)[:2]
      first_value = first_param_value(df, index, opcodeA, 1)
      second_value = first_param_value(df, index, opcodeB, 2)
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
      opcodeB, opcodeA = fill_command(command, 4)[:2]
      first_value = first_param_value(df, index, opcodeA, 1)
      second_value = first_param_value(df, index, opcodeB, 2)
      if instruction == 7:
        df.iloc[0, df.iloc[0, index + 3]] = 1 if first_value < second_value else 0
      else:
        df.iloc[0, df.iloc[0, index + 3]] = 1 if first_value == second_value else 0
      index += 4
    else:
      raise ValueError("unknown instruction")
  return amplifier_output


def moded_thruster_calculation(i, j, df, ind):
  amplifier_output, index = -1, ind
  i_flag = False
  while df.iloc[0, index] != 99:
    command = df.iloc[0, index]
    instruction = [int(d) for d in str(command)][-1]

    if instruction == 1 or instruction == 2:
      # Read Opcode
      opcodeB, opcodeA = fill_command(command, 4)[:2]
      first_value = first_param_value(df, index, opcodeA, 1)
      second_value = first_param_value(df, index, opcodeB, 2)

      # Read Instructions
      if instruction == 1:
        df.iloc[0, df.iloc[0, index + 3]] = first_value + second_value
      else:
        df.iloc[0, df.iloc[0, index + 3]] = first_value * second_value

      index += 4
    elif instruction == 3 or instruction == 4:
      opcode = fill_command(command, 3)[0]
      if instruction == 3:
        # user_ID = input("Please input user ID of the system you wish to test: ")
        if i_flag:
          df.iloc[0, df.iloc[0, index + 1]] = j
        else:
          df.iloc[0, df.iloc[0, index + 1]] = i
          i_flag = True
      else:  # instruction 4
        fpv = first_param_value(df, index, opcode, 1)
        index += 2
        yield fpv, df, True, index
      index += 2
    elif instruction == 5 or instruction == 6:
      opcodeB, opcodeA = fill_command(command, 4)[:2]
      first_value = first_param_value(df, index, opcodeA, 1)
      second_value = first_param_value(df, index, opcodeB, 2)
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
      opcodeB, opcodeA = fill_command(command, 4)[:2]
      first_value = first_param_value(df, index, opcodeA, 1)
      second_value = first_param_value(df, index, opcodeB, 2)
      if instruction == 7:
        df.iloc[0, df.iloc[0, index + 3]] = 1 if first_value < second_value else 0
      else:
        df.iloc[0, df.iloc[0, index + 3]] = 1 if first_value == second_value else 0
      index += 4
    else:
      raise ValueError("unknown instruction")
  yield j, df, False, index

def sec_moded_thruster_calculation(j, df, ind):
  amplifier_output, index = -1, ind
  i_flag = False
  while df.iloc[0, index] != 99:
    command = df.iloc[0, index]
    instruction = [int(d) for d in str(command)][-1]

    if instruction == 1 or instruction == 2:
      # Read Opcode
      opcodeB, opcodeA = fill_command(command, 4)[:2]
      first_value = first_param_value(df, index, opcodeA, 1)
      second_value = first_param_value(df, index, opcodeB, 2)

      # Read Instructions
      if instruction == 1:
        df.iloc[0, df.iloc[0, index + 3]] = first_value + second_value
      else:
        df.iloc[0, df.iloc[0, index + 3]] = first_value * second_value

      index += 4
    elif instruction == 3 or instruction == 4:
      opcode = fill_command(command, 3)[0]
      if instruction == 3:
        # user_ID = input("Please input user ID of the system you wish to test: ")
        df.iloc[0, df.iloc[0, index + 1]] = j

      else:  # instruction 4
        fpv = first_param_value(df, index, opcode, 1)
        index += 2
        yield fpv, df, True, index
      index += 2
    elif instruction == 5 or instruction == 6:
      opcodeB, opcodeA = fill_command(command, 4)[:2]
      first_value = first_param_value(df, index, opcodeA, 1)
      second_value = first_param_value(df, index, opcodeB, 2)
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
      opcodeB, opcodeA = fill_command(command, 4)[:2]
      first_value = first_param_value(df, index, opcodeA, 1)
      second_value = first_param_value(df, index, opcodeB, 2)
      if instruction == 7:
        df.iloc[0, df.iloc[0, index + 3]] = 1 if first_value < second_value else 0
      else:
        df.iloc[0, df.iloc[0, index + 3]] = 1 if first_value == second_value else 0
      index += 4
    else:
      raise ValueError("unknown instruction")
  yield j, df, False, index

def amp_cont_soft(og_x, perms):
  ts = []
  for perm in perms:
    x = og_x
    for z in perm:
      x = thruster_calculation(int(z), x)
    ts.append(x)
  return ts


if __name__ == '__main__':
  df = pd.read_csv('7.csv', header=None)
  acs = [''.join(p) for p in permutations('56789')]
  x = []
  for perm in acs:
    mem = [df.copy() for i in range(5)]
    rs4, nn, first_loop = 0, True, True
    while nn:
      if first_loop:
        rs0, mem[0], nn, index0 = next(moded_thruster_calculation(int(perm[0]), rs4, mem[0], 0))
        rs1, mem[1], nn, index1 = next(moded_thruster_calculation(int(perm[1]), rs0, mem[1], 0))
        rs2, mem[2], nn, index2 = next(moded_thruster_calculation(int(perm[2]), rs1, mem[2], 0))
        rs3, mem[3], nn, index3 = next(moded_thruster_calculation(int(perm[3]), rs2, mem[3], 0))
        rs4, mem[4], nn, index4 = next(moded_thruster_calculation(int(perm[4]), rs3, mem[4], 0))
        first_loop = False
      else:
        rs0, mem[0], nn, index0 = next(sec_moded_thruster_calculation(rs4, mem[0], index0))
        rs1, mem[1], nn, index1 = next(sec_moded_thruster_calculation(rs0, mem[1], index1))
        rs2, mem[2], nn, index2 = next(sec_moded_thruster_calculation(rs1, mem[2], index2))
        rs3, mem[3], nn, index3 = next(sec_moded_thruster_calculation(rs2, mem[3], index3))
        rs4, mem[4], nn, index4 = next(sec_moded_thruster_calculation(rs3, mem[4], index4))
    x.append(rs4)
  print(max(x))

