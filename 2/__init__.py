import pandas as pd


def function(df):
  """
	Do Something
	"""
  for i in range(0, len(df.columns), 4):
    command = df.iloc[0, i]
    if command == 1 or command == 2:
      first_value = df.iloc[0, df.iloc[0, i+1]]
      second_value = df.iloc[0, df.iloc[0, i + 2]]
      if command == 1:
        df.iloc[0, df.iloc[0, i + 3]] = first_value + second_value
      else:
        df.iloc[0, df.iloc[0, i + 3]] = first_value * second_value
    elif command == 99:
      break
    else:
      raise ValueError("unknown command")
  return df.iloc[0, 0]


def reverse_eng(x, y):
  df = pd.read_csv('input.csv', header=None)
  df.iloc[0, 1] = x
  df.iloc[0, 2] = y
  return function(df) == 19690720

if __name__ == '__main__':
  for i in range(100):
    for j in range(100):
      if reverse_eng(i, j):
        print("Noun is {} and Verb is {}. Answer is {}".format(i, j, 100 * i + j))
        exit(1)

