#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = [9, 9, 9, 9, 7, 1, 2, 3, 5, 2, 8, 99, 101]


'''
Insertion sort
Runtime complexity: iteration over array of length n and switching at most k pairs for each iteration (by definition of the given array), takes O(n • k).
If k is constant and relatively small we can argue that it's actually close to a linear O(n) case.

Space complexity: constant O(1), all we need is 2 indices.
'''
def insertion_sort(list):
	for index in range(1,len(list)):
		value = list[index]
		i = index - 1 # index of the item directly to the left 
		while i >= 0 and (value < list[i]):
			if value < list[i]:
				list[i+1] = list[i] #shift number in slot i right to slot i+1
				list[i] = value # shift value left into slot i
				i = i - 1
			else: 
				break
	return list

print(insertion_sort(a))	

'''
Assumes that L is a list of elements that can be compared using >.
Sorts in ascending order.
''' 
def selection_sort(L):
	suffixStart = 0
	while suffixStart != len(L):
		for i in range(suffixStart, len(L)):
			if L[i] < L[suffixStart]:
				L[suffixStart], L[i] = L[i], L[suffixStart]
		suffixStart += 1
	return L

print(selection_sort(a))

'''
Counting sort takes O(n)O(n) time and O(n)O(n) additional space (for the new list that we end up returning).

1. Allocate a list nums_to_counts where the indices represent numbers from our input list and the values represent
how many times the index number appears. Start each value at 0.
2. In one pass of the input list, update nums_to_counts as you go, so that at the end the values in nums_to_counts are correct.
3. Allocate a list sorted_list where we'll store our sorted numbers.
In one in-order pass of nums_to_counts put each number, the correct number of times, into sorted_list.
'''
def counting_sort(the_list, max_value):

	# 1. 
	# list of 0s at indices 0..max_value
	nums_to_counts = [0] * (max_value + 1)
	print(nums_to_counts)

	# 2.
	# The index in the actual number (item), and the 
	# value is the number of times it appears in the list
	for item in the_list:
		nums_to_counts[item] += 1

	print(nums_to_counts)

	# 3. 
	# populate the final sorted list
	sorted_list = []

	for item, count in enumerate(nums_to_counts):
		for time in range(count):
			sorted_list.append(item)

	return sorted_list

print(counting_sort(a, 101))


'''
Merge sort
'''

def merge(lef, right, compare):
	""" Assumes left and right are sorted lists and compare 
		defines an ordering on the elements. 
		Retuns a new sorted (by compare) list containing the same elements
		as (left + right) would contain.
	"""

	result = []
	i, j = 0, 0
	while i < len(left) and j < len(right):
		if compare(left[i], right[j]):
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	while (i < len(left)):
		result.append(left[i])
		i += 1
	while (j < len(right)):
		result.append(right[j	])
		j += 1

	return result

import operator

def merge_sort(the_list, compare = operator.lt):
	if len(the_list) < 2:
		return the_list[:]

	else:
		middle = len(the_list) // 2
		print("dkjskdjs" + str(middle))
		left = merge_sort(the_list[:middle], compare)
		right = merge_sort(the_list[middle:], compare)
		return merge(left, right, compare)

def msort4(x):
    result = []
    if len(x) < 20:
        return sorted(x)
    mid = len(x)//2
    y = msort4(x[:mid])
    z = msort4(x[mid:])
    i, j = 0, 0
    while i < len(y) and j < len(z):
            if y[i] > z[j]:
                result.append(z[j])
                j += 1
            else:
                result.append(y[i])
                i += 1
    result += y[i:]
    result += z[j:]
    return result
print(msort4(a))







