a = [9, 7, 1, 3, 5, 2, 8]

def largest_item_in_list(list):

	for index in range(1, len(list)):
		value = list[index]
		i = index - 1
		while i >= 0 and (value < list[i]):
			if value < list[i]:
				list[i+1] = list[i] #shift number in slot i right to slot i+1
				list[i] = value # shift value left into slot i
				i = i - 1

	return list[-1]

print(largest_item_in_list(a))

def smallest_item_in_list(list):

	for index in range(1,len(list)):
		value = list[index]
		i = index - 1
		while i >= 0 and (value < list[i]):
			if value < list[i]:
				list[i+1] = list[i] #shift number in slot i right to slot i+1
				list[i] = value # shift value left into slot i
				i = i - 1

	return list[0]

print(smallest_item_in_list(a))