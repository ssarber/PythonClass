def histogram(s):
    d = dict()
    for c in s:

    	# d.get(c, 0) returns value for c or else 0 if c is not in the dict
        d[c] = d.get(c, 0) + 1
    return d
    
s = ["a", "a", "b", "c", "c"]

print(histogram(s))
        