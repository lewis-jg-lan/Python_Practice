data = open('sketch.txt')

for each_line in data:
	(role,line_spoken) = each_line.split(':')
	print(role,end='')
	print(' said: ',end='')
	print(line_spoken,end='')

data.close()

def in_fridge():
	"""This is a function to see if the fridge has a food.fridge has to be a dictionary defined outside of the function,the food to be searched for is in the string wanted_food"""
	try:
		count = fridge[wanted_food]
	except KeyError:
		count = 0
		raise
	finally:
		return count


print("\n\n%s\n" % in_fridge.__doc__)
fridge = {"you":1,"wanted_food":2}


print(dir())

