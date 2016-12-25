def things():
	try:
		result = thing[I_wanted]
	except Exception, e:
		print('Please don\'t give up,try again!')
		raise	
	return result

thing = {"Job":"programming","Pay":"more","Motion":"happy"}
I_wanted = "Job"
things()

def in_fridge():
	try:
		count = fridge[wanted_food]
	except KeyError:
		count = 0
	return count

fridge = {"You":"I","Can":"Belive","Do":"In","It":"You"}
wanted_food = "You"
in_fridge()



