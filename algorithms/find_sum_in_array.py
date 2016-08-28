
arr = [0, 2, 3, 5, 6, 9, 8, 10, 12]
s = 5

'''
Brute force
Loop over the array and compare each number with 
all the other numbers and see if they sum up to the number
Time complexity: 0(n)
'''
def find_sums_of_x_in_array_brute(s, arr):
	i = 0
	j = 0

	for i in range(len(arr)):
		for j in range(len(arr)):
			if arr[i] + arr[j] == s:
				print("Found a pair: " + str(arr[i]) + "," + str(s-arr[i]))
			j += 1
		i += 1
			

'''
For each number X in the array, see if there is a s-X
in that array, and use binary search for it.
Time complexity: 0(log n)
'''
def find_sums_of_x_in_array(s, arr):
	pair = ()
	sums = []
	for i in range(len(arr)):

		found = binary_search(arr, s-arr[i])

		if found:
			print("Found a pair: " + str(arr[i]) + "," + str(s-arr[i]))
			pair = (arr[i], s-arr[i])
			sums.append(pair)
	return sums


def find_sums_of_x_using_dict(flight_len, movie_lengths):
	movie_lengths = dict(movie_lengths)
	keys = movie_lengths.keys()

	print(keys)
    
	for i in range(len(keys)):
		diff = flight_len - i
        found = diff in movie_lengths
        if found:
        	return True
	return False


def binary_search(arr, num):

	start = 0
	end = len(arr) - 1

	while start < end:
		middle = (start + end) // 2
		if num > arr[middle]:
			start = middle + 1
		elif num == arr[middle]:
			return True
		else:
			end = middle
	return False

print(binary_search(arr, 10))
print(find_sums_of_x_in_array_brute(13 , arr))

print(find_sums_of_x_in_array(13, arr))

def list_to_dict(li):  
	d = {k:v for k,v in (x.split(':') for x in li) }

li = [1, 1, 1, 2, 3, 3, 4, 4, 4, 4, 4, 5, 6, 7, 7]  
print("List to dict: " + str(list_to_dict(li)))

# print(find_sums_of_x_using_dict(8, {1: True, 2: True, 3: True, 4: True}))


# public interface TwoSum {
#     /**
#      * Stores @param input in an internal data structure.
#      */
#     void store(int input);
 
#     /**
#      * Returns true if there is any pair of numbers in the internal data structure which
#      * have sum @param val, and false otherwise.
#      * For example, if the numbers 1, -2, 3, and 6 had been stored,
#      * the method should return true for 4, -1, and 9, but false for 10, 5, and 0
#      */
#     boolean test(int val);
# }


# store(1)
# store(2)
# test(3) -> true
# test(4) -> false
# store(3)
# test(4) -> true

# class TwoSum:

#     hash_map = []
    
    
#     //hash_map.append(key, value)
#     //hash_map.append(2, true)
    
#     //hash_map.get(2) -> true or false
    
    
    
    
#     hash_map = [];
#     hash_map.append(3, true);
#     hash_map.get(3) //returns true
    
#     def store(input):
#         hash_map = [] //created
#         hash_map.append(input, True)    
        
#     def test(val):
#         # Brute force
#         # Loop over array and add every other number
#         # and see if they sum up to the input
        
        
#         #transform arr into a hash map
#         #do lookups on this hash map
        

#         sums = []
#         pair = ()
#         i = 0
#         j = 0
        
#         //1,2,3,4,6,7
#         //7   
        
#         keys = hash_map.keys() //[1, 2, 3, 4, 6, 7]     
        
#         for i in range(len(keys)):
#             diff = val - i
#             found = hash_map.get(diff)
            
#             if (found) {
#                 return true
#             }
#             i += 1
                     
#         return false
        
         
        
    
    
    

