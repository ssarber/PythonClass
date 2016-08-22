
arr = [0, 2, 3, 5, 6, 9, 8, 10, 12]
s = 5

# Brute force
# Loop over the array and compare each number with 
# all the other numbers and see if they sum up to the number
def find_sums_of_x_in_array_brute(s, arr):
	i = 0
	j = 0

	for i in range(len(arr)):
		for j in range(len(arr)):
			if arr[i] + arr[j] == s:
				print("Found a pair: " + str(arr[i]) + "," + str(s-arr[i]))
			j += 1
		i += 1
			



def find_sums_of_x_in_array(s, arr):
	# for every mumber x in the array, find all numbers that are s-x
	pair = ()
	sums = []
	for i in range(len(arr)):

		found = binary_search(arr, s-arr[i])

		if found:
			print("Found a pair: " + str(arr[i]) + "," + str(s-arr[i]))
			pair = (arr[i], s-arr[i])
			sums.append(pair)
	return sums



def binary_search(arr, num):

	start = 0
	end = len(arr) - 1

	while start < end:
		middle = (start + end) // 2
		if num > arr[middle]:
			start = middle + 1
		elif num == arr[middle]:
			return True
		else:
			end = middle
	return False

print(binary_search(arr, 10))
print(find_sums_of_x_in_array_brute(50, arr))

print(find_sums_of_x_in_array(13, arr))

for i in arr:
	print i
for i in range(len(arr)):
	print arr[i]
