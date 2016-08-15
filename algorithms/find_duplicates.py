

def find_duplicates(arr1, arr2):
	duplicates = []

	for number in arr1:
		if bSearch(arr2, number):
			duplicates.append(number)

	return duplicates

def bSearch(arr, num):
	begin = 0
	end = len(arr) - 1

	while (begin <= end):
		mid = (begin + end) // 2

		if (arr[mid] < num):
			begin = mid + 1
		elif arr[mid] == num:
			return True
		else:
		 	end = mid - 1

	return False


def findDuplicatesBrute(arr1, arr2):   
   duplicates = []
   i = 0
   j = 0
   while i < len(arr1) and j < len(arr2):
      if arr1[i] == arr2[j]:
         duplicates.append(arr1[i])
         i = i + 1
         j = j + 1
      elif arr1[i] < arr2[j]:
         i = i + 1
      else:
         j = j + 1
   return duplicates



a = [1, 2, 3, 4, 5, 6, 9, 10]
b = [1, 0, 2, 3, 4, 6, 9]

print(find_duplicates(a, b))
print(findDuplicatesBrute(a, b))

def find_duplicates(a, b):
   # naive is to linearly search and find matches
   duplicates = []

   for i in a:
      for j in b:
         if i == j:
            # match is both i and j
            duplicates.append(j)
   return duplicates

print(find_duplicates(a, b))
