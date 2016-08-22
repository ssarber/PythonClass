
# Reverse string
def reverse(text):
	lst = []
	position = 1

	for i in range(len(text)):
		print i
		lst.append(text[len(text) - position])
		position += 1

	lst = ''.join(lst)

	return lst

print(reverse("hello"))


# Create an array with duplicates from two arrays

def dedupe(arr1, arr2):
	merged_arr = arr1 + arr2

	deduped = set(merged_arr)

	return deduped

arr1 = [1, 2, 4, 5, 6]
arr2 = [1, 2, 4, 9, 10]
print(dedupe(arr1, arr2))


def bSearch(arr, num):
	begin = 0
	end = len(arr) - 1

	while (begin <= end):
		print "Iteration!!!"
		mid = (begin + end)//2

		if arr[mid] < num:
			begin = mid + 1
		elif arr[mid] == num:
			return True
		else:
			end = mid - 1

	return False

a = [1, 2, 5, 8, 13, 15, 18, 20]
print(bSearch(a, 15))


def findDuplicates(arr1, arr2):

	duplicates = []

	for number in arr1:
		print "Iteracion...."
		if bSearch(arr2, number):
			duplicates.append(number)
	return duplicates

a = [1, 2, 5, 8, 13, 15, 18, 20, 21]
b = [1, 5, 8, 15, 21]

print(findDuplicates(a, b))



def add(arr):
    sum = 0
    for num in arr:
    	print "Num: " + str(num)
        sum = sum + long(num)
        print str(sum)
    return sum

arr = [1,2,3,4]
print(add(arr))

a = [7, 1, 3, 5, 2, 8]
expected = [1, 2, 3, 5, 7, 8]

def array_sort(a):
	for i in range(1, len(a)):
		if a[i-1] > a[i]:
			tmp = a[i]
			a[i] = a[i -1]
			a[i-1] = tmp
	return a




print(array_sort(a))
