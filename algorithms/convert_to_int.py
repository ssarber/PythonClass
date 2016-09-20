# 1. Fibinacci

def fibo_recursive(n):
	if n in [0, 1]:
		return n
	return fibo_recursive(n-2) + fibo_recursive(n-1)


# 2. Implement LinkedList 
# - Is it a singly or doubly linked list?

class LinkedListNode:
	def __init__(self, value):
		self.value = value
		self.next = None

		# in a doubly linked list
		self.previous = None

	def get_value(self):
		return self.value

	def delete_node(self, n):
		node = LinkedListNode(n)
		node = None

a = LinkedListNode(2)
b = LinkedListNode(3)
a.next = b

l = LinkedListNode(2)
# l.delete_node()
# 3. Convert String to Int.
# Questions (think about edge cases):
# - Is the string an integer or can it be a floating point?
# - Do we need to handle negatives?
# - Do we need to handle special numbers like e, pi?
'''
Given "123" --> 123

string_list = [1, 2, 3]
s = 2
value = 12

'''

def to_int(string):

	if not isinstance(string, str) or string == "":
		raise Exception("Input must be a non-empty string.")

	string_list = list(string)

	is_positive = False
	if string_list[0] != "-":
		is_positive = True

	# This is what I will be returning later
	value = 0

	if is_positive:
	for s in string_list:
		if is_positive:
			value = value * 10 + int(s)
			print(value)
		else:
			
	else:
		print("Boo")
		nums_arr = string_list[1:]
		for s in nums_arr:
			value = value * 10 + int(s)
			print(value)
		value = value * -1


	return value


print(to_int("123"))