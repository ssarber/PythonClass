""" 1) Difference between List and Set. 
Sets can't contain duplicates
Sets are unordered
In order to find an element in a set, a hash lookup is used (which is why sets are unordered). This makes __contains__ (in operator) a lot more efficient for sets than lists.
Sets can only contain hashable items (see #3). If you try: set(([1],[2])) you'll get a TypeError.
In practical applications, lists are very nice to sort and have order while sets are nice to use when you don't want duplicates and don't care about order.
"""


# 2) Remove duplicates from a List.

from sets import Set

old_list = [6,2,3,9,1,41,43,89,5, 5]
ma_string = 'gabcdefgg'

#  doesn't maintain order -- orders from 1 to ...
new_list = list(set(old_list))
print(new_list)

# maintaining order: generator function
def dedupe(items):
	# We create a new set
	seen = set()

	# Iterate over the collection of items
	for item in items:
		if item not in seen:
			yield item
			print(item)
			seen.add(item)

print("Yo, deduped string that maintans order: " + str((list(dedupe(ma_string)))))	
print("Yo, deduped list that maintans order: " + str((list(dedupe(old_list)))))

# # from a dictionary
# def dedupeDict(items, key=None):
# 	seen = set()
# 	for item in items:
# 		val = item if key is None else key(item)
# 		if val not in seen:
# 			yield item
# 			seen.add(val)


# # has_duplicates
# string = 'jasa'

# def has_duplicates(array):
# 	s = list(array) # convert to a list
# 	s.sort() 
# 	print(range(len(s)))
# 	for item in range(len(s)):
# 		# print("Iteration: {}".format(item))

# 		# if any 2 items next to each other are equal, we have duplicates
# 		if s[item] == s[item + 1]:
# 			return True
# 	return False

# print(has_duplicates(old_list))
# print(has_duplicates(string))

def square():
	n = 0
	while n < 4:
		print("in generator, ", n)
		yield n * n
		n += 1
# square();
# for i in square():
# 	print(i)

print(4 in square())

def fibo(n):
	i, j = 1, 2
	for _ in range(n):
		yield i
		i, j = j, i + j
 
for i in fibo(6):
	print(i)

