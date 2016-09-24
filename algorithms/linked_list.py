class LinkedListNode:
	"""docstring for LinkedListNode"""
	def __init__(self, value):
		self.value = value
		self.next = None


a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e


"""
find the kkth to last node.
Brute-force. O(n) time and O(1) space, where n is the length of the list.
"""
def kth_to_last_node(k, head):

	if k < 1:
		raise ValueError("Impossible to find less than first to last node: %s" % k)
	# Step 1: get the length of the list.
	# Start at 1, 0
	# else we'd fail to count the head node!
	list_length = 1
	current_node = head

	# Traverse the whole list 
	# counting all the nodes
	while current_node.next:
		current_node = current_node.next
		list_length += 1

		if k > list_length:
			raise ValueError("k is larger than the length of the linked list.")
	# STEP 2: walk to the targer node
	# calculate how far to go, from the head,
	# to get to the kth last node.
	how_far_to_go = list_length - k
	current_node = head
	for i in range(how_far_to_go):
		current_node = current_node.next

	return current_node.value

def delete_node(node):
	pass


print(kth_to_last_node(3, a))