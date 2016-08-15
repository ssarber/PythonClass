my_list = [1,2,3,4]

def sum_it(list):
	my_sum = 0
	for i in range(len(my_list)):
		my_sum += list[i]
	return my_sum

print(sum_it(my_list))



