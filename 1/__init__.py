import pandas as pd

def calculate_module_sum(df):
	"""
	Sum together the weight of all the modules
	"""
	sum = 0
	for module in df.itertuples():
		module_weight = module[1]
		adjusted_weight = int(module_weight/3) - 2
		fuel_weight = weigh_fuel(adjusted_weight)
		sum += adjusted_weight + fuel_weight
	return sum


def weigh_fuel(weight):
	"""
	Recursively calculate weight for fuel 
	"""
	if weight < 7:
		return 0
	else:	
		fuel_for_fuel_weight = int(weight/3)-2
		return fuel_for_fuel_weight + weigh_fuel(fuel_for_fuel_weight)

if __name__ == '__main__':
	df = pd.read_csv('input.csv', header=None)
	print(calculate_module_sum(df))

