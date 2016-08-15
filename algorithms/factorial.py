def factorial_iterative_for_loop(num):
	answer = 1
	for i in range(num):
		answer *= (i + 1)
	return answer

		
print(factorial_iterative_for_loop(4))

def factorial_iterative_while_loop(num):
	answer = 0
	while num > 1:
		answer *= num
		num -= 1
	return answer

print(factorial_iterative_while_loop(4))


def factorial_recursive(num):
	 if num <= 1:
	 	return 1

	 return num * factorial_recursive(num - 1)

print(factorial_recursive(4))

