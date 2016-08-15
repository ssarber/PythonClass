my_list = [1,2,3,4]


cubes = [x**3 for x in my_list]

print(cubes)

my_dict = {1: 1, 2: 2, 3: 3}

# dictionary comprehension
new_dict = {item: item * item for item in my_dict}

print(new_dict)

