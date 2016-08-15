#!/usr/local/bin/python3

# Split

a = 'My awesome string'

print(a.split(' '))

print(a.replace('y', 'o'))

def is_reverse(word1, word2):
	if len(word1) != len(word2):
		return False
	i = 0
	print(len(word1))
	j = len(word2) - 1

	while j >= 0: #walk word #1 forward and word #2 backward and compare each character
		if word1[i] != word2[j]:
			return False
		print word1[i], word2[j]
		i = i + 1
		j = j - 1
	return True

print(is_reverse('stop', 'pots'))


def is_palindrome(word):
	forward = word[::1]
	backward = word[::-1]

	return backward == forward

print(is_palindrome("jeej"))


def is_palindrome_recursive(word):
	if str <= 0:
		print("Too short to determine.")
	reversed_str = is_palindrome_recursive(word[1:] + word[0])

# def reverse_number(number):
# 	num_to_list = [int(x) for x in str(number)]
# 	if len(num_to_list) <= 0:
# 		return number

# 	reversed_num = num_to_list[1:] + num_to_list[0]

# 	return reversed_num

# # is_palindrome_recursive("jeej")

# reverse_number(12345)


def is_palindr(word):
	num_to_list = [str(x) for x in str(word)]
	reversed_word = reverse_word(num_to_list)
	return word == reversed_word

def reverse_word(word):
	word = str(word)
	if len(str(word)) <= 0:
		return word
	reversed_word = reverse_word(word[1:]) + word[0]
	# print("reversed_word is now: " + reversed_word)

	return reversed_word

# def mirror(num):
# 	li = list(str(num))
# 	length = len(li) - 1
# 	for i in range(length / 2):
# 		if li[i] != li[length - i]:
# 			print "NO"
# 		return




print(reverse_word(2123212))
print(is_palindr(12321))

