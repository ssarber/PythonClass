#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Find The Duplicates

Given two arrays of US social security numbers: Arr1 and Arr2 of lengths n and m respectively,
 how can you most efficiently compute an array of all persons included on both arrays?

Solve and analyze the complexity for 2 cases:
1. m ≈ n - lengths are approximately the same
2. m ≫ n - one is much longer than the other

========== Hints & Tips ============ 
* As in any array iteration, check for proper indices limit and for covering all elements within the array

* The answer does not specify if the arrays are sorted in order to practice your peer with thinking about it. 
Your peer should ask that, since it'ts relevant to the solution and they should sort the arrays if not sorted already

* If your peer is stuck, ask for the brute force solution and then ask how can you do better.
Another clue is to tell your peer that arrays are sorted - if that doesn'tt ring a bell, ask how can the sorted order be used

* If your peer is making mistakes about complexity try to see if they can detect it before being told. ask them to explain, 
and if it doesn't help you can ask: Are you sure?

Some of the solutions for this kind of question may involve hashing one array and then searching its hash table 
for every item of the second array. For the first case (about the same length) the joint linear scan is better 
since you don't need to build the hash and maintain it. For the second case (one array is much longer than the other) 
it doesn't make any sense.

"""

"""
========== Solution ==========
The brute force solution is looping over one array, then looping on the other for each number of the first while storing the matches. 
That involves O(n⋅m) runtime complexity - very inefficient.

1. m ≈ n
We can leverage the sorted order of the arrays and loop over both in-order at the same time. 
By increasing the index of the array with the current smaller value every time we can be sure not to miss any duplicate:

"""
# Complexity here is O(n*2) since we have two nested for loops
def find_duplicates_brute(arr1, arr2):
   # naive is to linearly search and find matches
   duplicates = []

   for i in arr1:
      for j in arr2:
         if i == j:
            # match is both i and j
            duplicates.append(j)
   return duplicates


def find_duplicates(arr1, arr2):
	duplicates = []

	for number in arr1:
		if bSearch(arr2, number):
         # print str(number)
			duplicates.append(number)

	return duplicates


def bSearch(arr, num):
	begin = 0
	end = len(arr) - 1

	while (begin <= end):
		mid = (begin + end) // 2

		if (arr[mid] < num):
			begin = mid + 1
		elif arr[mid] == num:
			return True
		else:
		 	end = mid - 1

	return False

a = [1, 2, 3, 4, 5, 6, 9, 10]
b = [1, 0, 2, 3, 4, 6, 9]

# print(find_duplicates_brute(a, b))

print(find_duplicates(a, b))
