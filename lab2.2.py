#!/usr/local/bin/python3
print('Content-type: text/html\n')


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

# print fib(5)  # => 5
# print fib(10) # => 55
# a = fib(3)
# print(a)

# print('<td>data</td>')
# numbers =list(range(50))
# for i in numbers:
# 	num = fib(i)
# 	print('<td>')
# 	print (num)
# 	print('</td>')

print(fib(6))