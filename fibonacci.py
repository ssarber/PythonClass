

# def fibonacci(n):
# 	if n == 1 return 1

# 	elif n == 0 return 0

# 	y = 1
# 	x = 2
# 	for x in range (0, n):
# 		x = 0 + 1



def factorial(num):
	# product = 1
	# for i in range(num):
	# 	product *= (i+1)

	 # return product
	 if num <= 1:
	 	return 1

	 return num * factorial(num - 1)

# print(factorial(5))

# def fibonacci(term):
# 	if term == 0 
# 		return 0
# 	elif term == 1
# 	 	return 1
# 	number = number + fibonacci(number - 1)

# Iterative: recreate a list of Fibonacci sequence
def fibonacci(n):
	terms = [0, 1]
	i = 2
	while i <= n:
		terms.append(terms[i-1] + terms[i-2])
		i = i + 1
	return terms[n]

def fibonacci_rec(n):
	if (n == 0): return 0
	if (n == 1): return 1

	return fibonacci_rec(n-1) + fibonacci_rec(n-2)


print(fibonacci_rec(5))