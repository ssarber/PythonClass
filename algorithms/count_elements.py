
# Count all elements in a list
def count(elements):
	counter = 0
	for i in range(len(elements)):
		counter = counter + 1
	return counter

print(count([1,2,3,4]))


# Count ones and twos in a string
def count_nums(string):

	#first, convert string to a list
	char_list = map(int, string)
	ones = 0
	twos = 0

	for i in range(len(char_list)):
		if char_list[i] == 1:
			ones += 1
		if char_list[i] == 2:
			twos += 1
	return [ones, twos]


print(count_nums("1232112342"))