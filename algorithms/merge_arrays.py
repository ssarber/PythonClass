import unittest

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
def merge_lists(my_list, alices_list):
	# 1. Compare first elements
	# Whichever smaller, goes first. Compare second one from the same array with the one if the other
	# array
	# Maintain indexes of numbers that have been merged.

	# Make an array big enough to hold all elements from both lists

	# if len(my_list) == 0:
	if not my_list:
		return alices_list
	if not alices_list:
		return my_list
	merged_list_size = len(my_list) + len(alices_list)
	print(merged_list_size)
	merged_list = [None] * merged_list_size

	current_index_alices = 0
	current_index_mine = 0
	current_index_merged = 0

	while current_index_merged < merged_list_size:
		if current_index_mine >= len(my_list):
			# Case: my list is exhausted
			merged_list[current_index_merged] = alices_list[current_index_alices]
			current_index_alices += 1

		elif current_index_alices >= len(alices_list):
			# Case: Alice's list is exhausted
			merged_list[current_index_merged] = my_list[current_index_mine]
			current_index_mine += 1

		elif my_list[current_index_mine] < alices_list[current_index_alices]:
			# Case: next comes from my list
			merged_list[current_index_merged] = my_list[current_index_mine]
			current_index_mine += 1

		else:
			# Case: next comes from Alice's list
			merged_list[current_index_merged] = alices_list[current_index_alices]
			current_index_alices += 1

		current_index_merged += 1

	return merged_list


# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)

    def test_lists_have_same_numbers(self):
    	actual = merge_lists([2, 4, 6], [2, 4, 6])
    	expected = [2, 2, 4, 4, 6, 6]



unittest.main(verbosity=2)