
# O(n)
def histogram(s):
	d = dict()
	# 1. Check if character is already in the dict.
	# 2. If not, give it a value of 1.
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d