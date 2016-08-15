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
      
    def total_cost_instance(self, item_one, item_two):
        return item_one + item_two


    @staticmethod
    def total_cost(item_one, item_two):
        return item_one + item_two


    @classmethod
    def items_sold():
        pass    

#######################################

s = Spam()
print(s.total_cost_instance(2, 2))

# Using a setter
s.silly_walk = 'dsdjskjd'

 # Using a getter
print(s.silly_walk)

# Using a static method
cost = Spam.total_cost(1, 2)
print(cost) 
