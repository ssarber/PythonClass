'''
Solution #1. Compare the sorted strings (converted to lists).
'''
def is_permutation(s, t):
	# if they're different lengths, they can't be permutations
	if len(s) != len(t):
		return False
	return sort(s) == sort(t)


def sort(s):
	content = list(s)

	return sorted(content)

print is_permutation("asdf", "fdsa")
print is_permutation("123", "321s")


'''
Solution #2. If the strings are of equal character count, 
count how many time each character appears (histogram!)
'''
def is_permutation_via_histogram(s, t):
	if len(s) != len(t):
		return False
	return histogram(s) == histogram(t)


def histogram(s):
	hist = dict()

	for char in s:
		print(char)
		if char not in hist:
			hist[char] = 1
		else:
			hist[char] += 1

	return hist

print(histogram("dshkdhshsddd"))

print is_permutation_via_histogram("asdf", "fdsa")