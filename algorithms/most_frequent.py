'''
 The mode is the value that appears most often in a set of data.
'''
def find_mode(the_list):
	mode = 0

	occurrences_dict = histogram(the_list)

	sorted_values = counting_sort(occurrences_dict.values(), len(occurrences_dict.values())-1)
	largest = sorted_values[-1]

	print(largest)
	for key, value in occurrences_dict.items():
		print(str(key) + " " + str(value))
		if value == largest:
			mode = key

	return mode

def counting_sort(the_list, max_value):

	#list of 0s at indices 0..max_value
	nums_to_counts = [0] * (max_value + 1)

	for item in the_list:
		nums_to_counts[item] += 1

	#populate the final sorted list
	sorted_list = []

	for item, count in enumerate(nums_to_counts):
		for time in range(count):
			sorted_list.append(item)
	return sorted_list


def histogram(the_list):
	hist = dict()
	for n in the_list:
		if n in hist:
			hist[n] += 1
		else: 
			hist[n] = 1
	return hist

a = [1, 2, 4, 5, 1, 4, 1, 5, 5, 5, 5]

print(find_mode(a))