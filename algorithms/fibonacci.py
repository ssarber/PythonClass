f = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# # Returns last term of the Fibonacci sequence
# Runtime: O(2^n)
def fibonacciRecursive(n):
    if n < 0:
        raise Exception("Input must be a positive integer.")
    if n in [0,1]:
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

print(fibonacciRecursive(-7))
print(fibonacciIterative(7))

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


# Fibo memoization

class Fibber:

    def __init__(self):
        self.memo = {}

    def fib(self, n):
        if n < 0:
            raise Exception("Can't be negative")

        if n in [0, 1]:
            return n

        if n in self.memo:
            return n

        result = self.fib(n-2) + self.fib(n-1)

        #memoize 
        self.memo[n] = result
        print(self.memo)
        return result

f = Fibber()
print(f.fib(7))