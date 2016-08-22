# > stack = [3, 4, 5]
# >>> stack.append(6)
# >>> stack.append(7)
# >>> stack
# [3, 4, 5, 6, 7]
# >>> stack.pop()
# 7
# >>> stack
# [3, 4, 5, 6]
# >>> stack.pop()
# 6
# >>> stack.pop()
# 5
# >>> stack
# [3, 4]


def test_happy_path():
	test_input = "hello world"
	expected = "world hello"
	actual = reverse_words_using_stack(test_input)

	return expected == actual

def test_one_word_only():
	test_input = "hello"
	expected = "hello"
	actual = reverse_words_using_stack(test_input)

	return expected == actual	

def test_spaces_only():
	test_input = "  "
	expected = ""
	actual = reverse_words_using_stack(test_input)

	return expected == actual

def test_empty_input():
	test_input = ""
	expected = None
	actual = reverse_words_using_stack(test_input)

	return expected == actual

def test_null_input():
	test_input = None
	expected = None
	actual = reverse_words_using_stack(test_input)

	return expected == actual


'''
Using a stack. Stacks are last-in, first-out
A stack of pancakes
'''
def reverse_words_using_stack(text):

	if text == None or len(text) == 0:
		return

	stack = []
	length = len(text)
	space = ' '
	index = 0
	while index < length:
		if text[index] != space:
			word_start = index
			while index < length and text[index] != space:
				index += 1
			stack.append(text[word_start:index])
			print(text[word_start:index])
		index += 1
	return " ".join(reversed(stack))

sentence = 'Hello World'
print(reverse_words_using_stack(sentence))

print(test_happy_path())
print(test_one_word_only())
print(test_spaces_only())
print(test_empty_input())
print(test_null_input())



def reverse_words_using_mirror(sentence):
	reversed_chars = mirror_reverse(sentence)

	print(reversed_chars)
	reversed_sen = []

	word_start = None
	for i in range(len(reversed_chars)):

		# Check if we've hit a space
		if reversed_chars[i] == " ":
			if (word_start != None):
				word = mirror_reverse(reversed_chars[word_start: i])
				print("Word 1: " + word)
				word_start = None

				reversed_sen.append(word)

		# Check if we're at the end of the sentence
		# If so, grab the current word_start and the 
		# current i as the end of the word
		elif i == len(reversed_chars) - 1:
			print("Word 2: " + word)
			if word_start != None:
				word = mirror_reverse(reversed_chars[word_start: i+1])
				reversed_sen.append(word)

		else:
			if word_start == None:
				word_start = i
				print("word_start is now " + str(word_start))

	reversed_sen = ' '.join(reversed_sen)

	return reversed_sen


def mirror_reverse(arr):
	arr = list(arr)
	start = 0
	end = len(arr) - 1
	tmp = None

	while start < end:
		tmp = arr[start]
		arr[start] = arr[end]
		arr[end] = tmp

		start += 1
		end -= 1
	arr = ''.join(arr)
	return arr

sentence = 'Hello Third World'
print(reverse_words_using_mirror(sentence))

