# Reverse string

str = 'hello'

print(str[4])

# def reverse(string):
# 	str_list = list(string)
# 	for l in str_list:
# 		print(l)
# 		reverse_str = []
# 		yield l
# 		str_list.append(l)

print(''.join(reversed(str)))

''' 
Solution 1: extended slice ([begin:end:step]): 
https://docs.python.org/3.4/whatsnew/2.3.html#extended-slices 
http://stackoverflow.com/questions/931092/reverse-a-string-in-python
'''

print("Extended slice: " + str[::-1]) # this is the solution

print(str[:-1])

a = range(10)

print(a[1:9:2])

print(str[1])

def reverse(str):
	if len(str) <= 0:
		return str
	print("String is now: " + str)
	new_string = reverse(str[1:]) + str[0]
	print("After the call: " + new_string)
	return new_string

print(reverse(str))


def is_reverse(word1, word2):
	if len(word1) != len(word2):
		return False
	i = 0
	j = len(word2) - 1

	while j >= 0:
		if word1[i] != word2[j]:
			return False
		print word1[i], word2[j]
		i = i + 1
		j = j - 1
	return True

print(is_reverse('stop', 'pott'))

def oneLinePalindrome(word):
	return word[::1] == word[::-1]


print(oneLinePalindrome("jeej"))
	
"""
Big O of this is O(n) (linear)
"""
def reverseBrute(text):
    lst = []
    count = 1

    for i in range(len(text)):

        lst.append(text[len(text) - count])
        count += 1

    lst = ''.join(lst) # this just converts the list into a string
    return lst

print reverseBrute('hello')

"""
Big O of this is O(n/2) (half of linear)
"""
def reverseBetter(arr):

	arr = list(arr) #Convert to a list since strings are immutable in python
	start = 0
	end = len(arr) - 1

	while start < end:
		arr[start] = arr[end]
		arr[end] = arr[start]
		start += 1
		end -= 1

	arr = ''.join(arr)

	return arr


print(reverseBetter('hello'))

def swap(a, b):
	temp = a
	a = b
	b = temp

	return (a, b)

print(swap(2, 3))

def test()
	

