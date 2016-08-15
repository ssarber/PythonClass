# coding: utf-8

# 
# Generator functions are like normal functions in most respects, and in fact are coded with normal def statements. 
# However, when created, they are compiled specially into an object that supports the iteration protocol.
# And when called, they don’t return a result: they return a result generator that can appear in any iteration context.


def createGenerator():
	mylist = range(4)
	for i in mylist:
		yield i * i
 
mygenerator = createGenerator()
print(next(mygenerator))
print(next(mygenerator)) # mygenerator is an object!
print(next(mygenerator))
print(next(mygenerator))

for i in mygenerator:
	print(i)