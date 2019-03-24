# import unittest


# # Question: how is this data represented?
# # i.e. as tuples with (start time, 30-minute increments)

# def merge_lists(my_list, alices_list):
#     """Combine the sorted lists into one large sorted list
#     Iterate over both list comparing elements and keeping track of indices
#     that have been merged
   
#     """
#     merged_list_length = len(my_list) + len(alices_list)
#     merged_list = [None] * merged_list_length
    
#     my_list_current_index = 0
#     alices_list_current_index = 0
#     merged_list_current_index = 0
    
#     while merged_list_current_index < merged_list_length:
#         if my_list_current_index >= len(my_list):
#             # Next one comes from Alice's list
#             merged_list[merged_list_current_index] = alices_list[alices_list_current_index]
#             alices_list_current_index += 1
#         elif alices_list_current_index >= len(alices_list):
#             # Next one comes from my list
#             merged_list[merged_list_current_index] = my_list[my_list_current_index]
#             my_list_current_index += 1
#         elif my_list[my_list_current_index] < alices_list[alices_list_current_index]:
#             # Next one comes from my list
#             merged_list[merged_list_current_index] = my_list[my_list_current_index]
#             my_list_current_index += 1
#         else:
#             # Next one comes from Alice's list
#             merged_list[merged_list_current_index] = alices_list[alices_list_current_index]
#             alices_list_current_index += 1
            
#         merged_list_current_index += 1
    

#     return merged_list


# # Tests

# class Test(unittest.TestCase):

#     def test_both_lists_are_empty(self):
#         actual = merge_lists([], [])
#         expected = []
#         self.assertEqual(actual, expected)

#     def test_first_list_is_empty(self):
#         actual = merge_lists([], [1, 2, 3])
#         expected = [1, 2, 3]
#         self.assertEqual(actual, expected)

#     def test_second_list_is_empty(self):
#         actual = merge_lists([5, 6, 7], [])
#         expected = [5, 6, 7]
#         self.assertEqual(actual, expected)

#     def test_both_lists_have_some_numbers(self):
#         actual = merge_lists([2, 4, 6], [1, 3, 7])
#         expected = [1, 2, 3, 4, 6, 7]
#         self.assertEqual(actual, expected)

#     def test_lists_are_different_lengths(self):
#         actual = merge_lists([2, 4, 6, 8], [1, 7])
#         exapected = [1, 2, 4, 6, 7, 8]
#         self.assertEqual(actual, expected)

#     def test_lists_have_same_numbers(self):
#         actual = merge_lists([2, 4, 6], [2, 4, 6])
#         expected = [2, 2, 4, 4, 6, 6]


# unittest.main(verbosity=2)
