#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = [9, 7, 1, 3, 5, 2, 8]


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

print(counting_sort(a, 9))







