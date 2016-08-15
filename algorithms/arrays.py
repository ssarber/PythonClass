def return_index(array):

	if len(array) < 3:
		return
	indices = []
	for i in range(len(array)):
		first_sum = array[i] + array[i + 1]
		middle_element_index = i + 2
		second_sum = array[i + 3] + array[i + 4]


		if first_sum == second_sum:
			return middle_element_index


array = [1, 1, 2, 1, 1, 3, 4]
print(return_index(array))


def reverse(word):
	lst = []
	count = 1

	for i in range(len(word)):
		lst.append(word[len(word) - count])
		count = count + 1

	lst = "".join(lst)
	return lst

print(reverse("hello"))


# def fizzbuzz():
# 	for i in range(100):
# 		if i % 3 == 0:
# 			print str(i) + " fizz"
# 		if i % 5 == 0:
# 			print str(i) + " buzz"
# 		if i % 15 == 0:
# 			print str(i) + " fizzbuzz"

# fizzbuzz()