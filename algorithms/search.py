"""
Binary search.
1. Split the array in two.
	- Define a start, end and middle of the array.
2. Look for the number in the first half of the array. If it's not there,
shift the search to the right, and reassign start, end and middle.
3. Repeat.

---> Don't confuse index with the value!!!!
"""

a = [2, 4, 1, 6, 9, 7, 10]

def binary_search(arr, num):
	start = 0
	end = len(arr) - 1

	while (start <= end):
		middle = (start + end) // 2
		if num > arr[middle]:
			start = middle + 1
		elif num == arr[middle]:
			return True
		else:
			end = middle

	return False

print(binary_search(a, 7))