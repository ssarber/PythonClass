
# # Returns last term of the Fibonacci sequence
def fibonacciRecursive(n):
    if n < 2:
        return n
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2)


# Returns last term of the Fibonacci sequence
def fibonacciIterative(n):
    terms = [0, 1]  # start from first two terms by definition
    i = 2
    while i <= n:
        terms.append(terms[i - 2] + terms[i - 1])
        # print(terms)
        i = i + 1
        # print("i" + str(i))
    return terms[n] # return last (n-th) integer in the list

print(fibonacciRecursive(7))
print(fibonacciIterative(7))


# def fibonacci(n):
#     a = 0
#     b = 1
#     seq = []
#     while b <=n:
#         seq.append(a)
#         seq.append(b)
#         a = b
#         b = a + `
#     return seq[n]
       
# print(fibonacci(8))

def fiboYield(n):
    i, j = 0, 1
    for _ in range(n):
        yield j
        i, j = j, i + j

def fib():
    i, j = 0, 1
    while True:
        yield i
        i, j = j, i + j

import itertools
print(list(itertools.islice(fiboYield(7), 7)))



# sorted(iterable, key=None)

# sorted([3,2,1]) -> [1,2,3]

# sorted([-6, 3, 5], key=lambda n: math.abs(n)) -> [3, 5, -6]


# [1] -> [1]

# [1, 99, 93, 2002, 88, 92] --> 
# [1.4, 2.3, 8.4]
# ["a", "b", "u"] 
# [[1,2,2], [1,2,3]]
# [1, "b", 1.2]
# [1, -9, -9.8, -9999999999]

# sorted([-6, 3, 5], key=lambda n: "b")