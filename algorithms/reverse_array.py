# Task 
# Given an array, A , of N integers, print A's elements in reverse order as a single line of space-separated numbers.

# Input Format

# The first line contains an integer, N (the size of our array). 
# The second line contains  space-separated integers describing array A's elements.

# Output Format

# Print the elements of array  in reverse order as a single line of space-separated numbers.


def reverse_arr(arr, n):
    index = n - 1
    new_arr = []
    for i in range(n):
        new_arr.append(arr[index])
        index -= 1
        
    return ' '.join(map(str, new_arr))

arr = [1, 4, 3, 2]
print(reverse_arr(arr, 4))
    

def total(pretax, tip_percent, tax_percent):
    total = pretax + pretax * tip_percent + pretax * tax_percent
    return int(round(total))

print("The total meal cost is {} dollars.".format(total(12, 0.2, 0.08)))