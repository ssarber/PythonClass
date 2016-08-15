""" 1) Difference between List and Set. 
Sets can't contain duplicates
Sets are unordered
In order to find an element in a set, a hash lookup is used (which is why sets are unordered). This makes __contains__ (in operator) a lot more efficient for sets than lists.
Sets can only contain hashable items (see #3). If you try: set(([1],[2])) you'll get a TypeError.
In practical applications, lists are very nice to sort and have order while sets are nice to use when you don't want duplicates and don't care about order.
"""

# 2) Remove duplicates from a List.

from sets import Set

old_list = [6,2,3,3,1,4,4,4,5]

#  doesn't maintain order -- orders from 1 to ...
new_list = list(Set(old_list))

print(new_list)

# maintaining order
def dedupe(items):
	seen = set()
	for item in items:
		if item not in seen:
			yield item
			print(item)
			seen.add(item)
	
print(list(dedupe(old_list)))

# from a dictionary
def dedupeDict(items, key=None):
	seen = set()
	for item in items:
		val = item if key is None else key(item)
		if val not in seen:
			yield item
			seen.add(val)


# a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]

# print(list(dedupeDict(a, key=lambda d: (d['x'],d['y']))))

########## 3) Test case: sign up. Randomly-generated postfix for email address (timestamp)

# Modules time and datetime

# imaplib for Gmail
# try:
#     M.login('email@gmail.com', getpass.getpass())
# except imaplib.IMAP4.error:
#     print "LOGIN FAILED!!! "
#     # ... exit or deal with failure...


# MySQL: 
# MySQLdb library

# select * from users where email like 'test%'


######### 4)
# Design front-end testing framework: page object model


########## 5) Location strategies

########### 6) JSON. what library to use in python?

############ 7) How to create a constructor and declare instance variables in a regular python class?

############ 8) 

# "xpath=//div[{$divNumber}]/table/tbody/tr/td[4]/div/a/span"

###### In Angualar, what is a directive? What's a directive for model, controller, app?


######### JavaScript ###########

# What are global variables? How are they declared?

# local: var bob;
# global: bob // no "var"

# Comparison operators: difference betwee two equals signs and three?
 # == equal value
 # ===	equal value and equal type

def frange(start, end, increment):
	x = start
	while x < end:
		yield x
		x += x

# for i in frange(1, 11, 2):
# 	print(i)


