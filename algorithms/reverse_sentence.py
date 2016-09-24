'''
"air the in is sunshine"
--> "sunshine is in the air"
Approach: 
1. write a helper function that reversed any
list of characters.
2. reverse the whold sentence.
3. Iterate over reversed sentence and use the same function
to reverse each word.
'''

def reverse_words(message):
	# Convert the message to a list
	message_list = list(message)

	# Reverse the list in-place
	reverse_characters(message_list, 0, len(message_list) - 1)

	print(message_list)

	# Initialize a var to keep track of word start index
	current_word_start_index = 0

	for i in range(len(message_list) + 1):
		if (message_list[i] == " ") or (i == len(message_list)):

			reverse_characters(message_list, current_word_start_index, i-1)

			current_word_start_index = i + 1

	return ' '.join(message_list)



def reverse_characters(message_list, front_index, back_index):
	while front_index < back_index:
		message_list[front_index], message_list[back_index] = \
			message_list[back_index], message_list[front_index]
		front_index += 1
		back_index -= 1
	# print(message_list)
	return message_list


a = "air the in is sunshine"
# print(reverse_characters(list(a), 0, len(a)-1))
print(reverse_words(a))

# def test_happy_path():
# 	test_input = "hello world"
# 	expected = "world hello"
# 	actual = reverse_words_using_stack(test_input)

# 	return expected == actual

# def test_one_word_only():
# 	test_input = "hello"
# 	expected = "hello"
# 	actual = reverse_words_using_stack(test_input)

# 	return expected == actual	

# def test_spaces_only():
# 	test_input = "  "
# 	expected = ""
# 	actual = reverse_words_using_stack(test_input)

# 	return expected == actual

# def test_empty_input():
# 	test_input = ""
# 	expected = None
# 	actual = reverse_words_using_stack(test_input)

# 	return expected == actual

# def test_null_input():
# 	test_input = None
# 	expected = None
# 	actual = reverse_words_using_stack(test_input)

# 	return expected == actual

# print(test_happy_path())
# print(test_one_word_only())
# print(test_spaces_only())
# print(test_empty_input())
# print(test_null_input())

