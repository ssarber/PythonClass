
arr = [0, 2, 3, 5, 6, 9, 8, 10, 12]
s = 5

'''
Brute force
Loop over the array and compare each number with 
all the other numbers and see if they sum up to the number
Time complexity: 0(n)
'''
def find_sums_of_x_in_array_brute(s, arr):
	i = 0
	j = 0

	for i in range(len(arr)):
		for j in range(len(arr)):
			if arr[i] + arr[j] == s:
				print("Found a pair: " + str(arr[i]) + "," + str(s-arr[i]))
			j += 1
		i += 1
			

'''
For each number X in the array, see if there is a s-X
in that array, and use binary search for it.
Time complexity: 0(log n)
'''
def find_sums_of_x_in_array(s, arr):
	pair = ()
	sums = []
	for i in range(len(arr)):

		found = binary_search(arr, s-arr[i])

		if found:
			print("Found a pair: " + str(arr[i]) + "," + str(s-arr[i]))
			pair = (arr[i], s-arr[i])
			sums.append(pair)
	return sums


def find_sums_of_x_using_set(flight_len, movie_lengths):
	movie_lengths_seen = set()

	for first_movie_time in movie_lengths:
		second_movie_time = flight_len - first_movie_time
		if second_movie_time in movie_lengths_seen:
			return True
		movie_lengths_seen.add(first_movie_time)

	return False

arr = [0, 2, 3, 5, 6, 9, 8, 10, 12]
print(find_sums_of_x_using_set(30, arr))


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

# -*- coding: utf-8 -*-
"""
We can use a set if we won't be storing any duplicates.
Otherwise, it appears that we'll need a dict() and store int as keys.
"""

class MyData:

	hash_set = set()
	the_list = []
	
	def store(self, val):
		self.hash_set.add(val)


	def remove(self, val):
		if val in self.hash_set:
			self.hash_set.remove(val)
	   
	def get_random(self):
		import random
		return random.sample(self.hash_set, 1)

	def see_if_sum_exists(self, val):


		# keys = self.hash_set.keys()

		# for i in keys:
		# 	diff = val - i

		# 	found = self.hash_set.get(diff, None)

		# 	if found:
		# 		return True
		# return False

		seen = set()
		for first_int in self.hash_set:
			second_int = val - first_int
			if second_int in seen:
				return True

			seen.add(first_int)

  
d = MyData()
d.store(3)
print(d.hash_set)
d.store(4)
d.store(5)
d.store(6)

print(d.hash_set)

print(d.see_if_sum_exists(7))
print(d.get_random())
		
		 
	
	
	

