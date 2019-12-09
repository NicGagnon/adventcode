import pandas as pd


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




if __name__ == '__main__':
  df = pd.read_csv('input.csv', header=None)
  index = 0

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
        user_ID = input("Please input user ID of the system you wish to test: ")
        df.iloc[0, df.iloc[0, index + 1]] = int(user_ID)
      else:                                 # instruction 4
        print(first_param_value(df, index, opcode, 1))
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
      else:                                 # instruction 6
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

  print("the program as terminated")
