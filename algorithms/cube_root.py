x = 1957816251

# Exhaustive enumeration
ans = 0
while ans**3 < abs(x):
	ans = ans + 1
if ans**3 != abs(x):
	print x, "is not a perfect cube"

else:
	if x < 0:
		ans = - ans
	print "Cube root of", x, "is", ans