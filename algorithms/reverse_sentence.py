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

'''
Using a stack. Stacks are last-in, first-out
A stack of pancakes
'''
def reverse_words_using_stack(text):
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

sentence = 'Hello World'

reversed_str = sentence[::-1]

print(reversed_str)

