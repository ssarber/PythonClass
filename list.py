# ********* Final  *************#


class Spam:

	def __init__(self):
		# self._silly_walk = None
		pass

	@property
	def silly_walk(self):
		return self._silly_walk.upper()

	# Setter
	@silly_walk.setter
	def silly_walk(self, value):
		print("silly_walk setter")
		self.silly_walk = value.upper()

	# Static method
	@staticmethod
	def total_cost(item_one, item_two):
		return item_one + item_two

	# Class method
	@classmethod
	def items_sold(item_one, item_two):
		return item_one + item_two	

s = Spam()

# Using a setter
s._silly_walk = 'lower character string'

# Using a getter
print(s.silly_walk)

# Using a static method
cost = Spam.total_cost(1, 2)
print(cost)


class Spam():

    def __init__(self):

        #self._silly_walk = None
        pass
    

    @property
    def silly_walk(self):

        print("silly_walk getter")

        return self._silly_walk
  

    @silly_walk.setter
    def silly_walk(self, value):

        print("silly_walk setter")

        self._silly_walk = value.upper()

        

    @staticmethod
    def total_cost(item_one, item_two):

        return item_one + item_two



    @classmethod
    def items_sold():

        pass    

s = Spam()


# Using a setter
s.silly_walk = 'dsdjskjd'

 # Using a getter
print(s.silly_walk)

# Using a static method
cost = Spam.total_cost(1, 2)
print(cost) 
