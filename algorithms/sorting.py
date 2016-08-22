
a = [9, 7, 1, 3, 5, 2, 8]


"""
Insertion sort
Runtime complexity: iteration over array of length n and switching at most k pairs for each iteration (by definition of the given array), takes O(n • k).
If k is constant and relatively small we can argue that it's actually close to a linear O(n) case.

Space complexity: constant O(1), all we need is 2 indices.
"""
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


from bisect import bisect_left

def in_bisect(word_list, word):
    """Checks whether a word is in a list using bisection search.

    Precondition: the words in the list are sorted

    word_list: list of strings
    word: string
    """
    i = bisect_left(word_list, word)
    if i != len(word_list) and word_list[i] == word:
        return True
    else:
        return False

print(in_bisect(a, 10))

a = True or False
print(a)