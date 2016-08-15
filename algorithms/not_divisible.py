
# is the number divisible by 2 and 3?
def divisible(n):
	return n % 2 == 0 and n % 3 == 0

print(filter(divisible, range(2, 25)))

def not_divisible(n):
	return n % 2 != 0 and n % 3 != 0

print(filter(not_divisible, range(2, 25)))
