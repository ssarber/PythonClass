'''
Lists:
* unordered, mutable, can contain duplicates

Sets:
* unordered, mutable, can't contain duplicates

Tuples: 
*immutable
'''

string = 'zjsdjsjdkjksjd'
def both_ends(s):
  # +++your code here+++
  if s<2:
    return ""
  return s[:2]+s[:-2]

print(both_ends("abcdefg"))

print(string[:1])


a = [1,2,3,4]
a.append(5)
print(a[4])

my_str = 'abracadabra'
my_list = [1,2,3,4]

# Removes unwanted characters
b = [x for x in my_str if x not in 'a']
c = [x for x in my_list if x not in [1,2]]

print(b)
print(c)

l = sorted([3,1,4,6])
l.append(1)
print(l)