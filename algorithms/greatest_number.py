

def greatest(l):
	maximum = 0
	for i, value in enumerate(l) :
		print(i, value)
		if value > maximum:
			maximum = value

			# print(value)

	return maximum


l = [15,10,1,2,8,3,1,9, 11]

print(greatest(l))