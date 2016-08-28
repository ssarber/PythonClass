# a = [1,2,3,4,55,]
# b = [1,2,3,4,5,6,6]


# # merge the lists and convert them to  set, and eliminate the duplicates
# merged_list = a + b
# merged_set = set(merged_list)
# # merged_set = first_words_set.union(last_words_set)

# print('\n\n' + 'There are {} unique words in both lists:'.format(len(merged_set)) + '\n')
# print(merged_set)

'''
Determine if a string has all unique characters.
'''
import unittest

# O(N)
def unique(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_dict = {}

    for char in string:
        if char_dict.get(char, 0) != 0:
            return False
         # add all chars to the dict as keys with values of True
        char_dict[char] = True

    return True

print(unique("kwertyk"))

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = unique(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = unique(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()