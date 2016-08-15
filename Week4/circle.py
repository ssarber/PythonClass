import math
from random import randint

def main():
    # run some tests here.
    """Testing Circle class for area(), move(), 
    location(), __str__()"""
    i2 = 0
    c1 = Circle(0, 0, 20)
    c2 = Circle(0, 0, 20)
    for i in range(20):
        print('--')
        # print('Circle 1: ',c1)
        # print('Circle 2: ',c2)
        print("Collision? ",Circle.is_collision(c1, c2))
        print(Circle.is_collision(c1, c2))
        i2 += i
        c1.move(i, i)
        c2.move(i, i2)

class Shape():
    """Shape class provides a move() method."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #  generate random coordinates
    def move(self, x, y):
        self.x = randint(0, 70);
        self.y = randint(0, 70);

    def location(self):
        return self.x, self.y

class Circle(Shape):
    """Circle is a sub-class of shape and inherits the move()
    method"""
    def __init__(self, x=0, y=0, radius=1):
        """Call the parent class constructor with x,y coords."""
        Shape.__init__(self, x, y)  
        self.radius = radius

    def area():
        pass # fill this in

    def __str__(self):
        pass # fill this in

    @classmethod
    # If the distance between the centers of the two circles is less than 
    # or equal to the sum of the radii, the two circles are colliding.
    def is_collision(Circle, c1, c2):
        sum_of_radii = c1.radius + c2.radius
        # print("Sum %d" %sum_of_radii)

        return True if Circle.distance(c1, c2) < sum_of_radii  else False


    @classmethod
    def distance(Circle, c1, c2):

        """calculate distance between two circles"""
        cir_1_coord = c1.location()
        cir_2_coord = c2.location()
        print(cir_1_coord)
        print(cir_2_coord)

        cir1_x = cir_1_coord[0]
        cir1_y = cir_1_coord[1]

        cir2_x = cir_2_coord[0]
        cir2_y = cir_2_coord[1]

        # sides a and b to calculate distance between centers of circles via Pythagorean theorem
        a = math.fabs(cir1_x - cir2_x)
        b = math.fabs(cir1_y - cir2_y)

        distance = math.sqrt(a * a + b * b)
        return distance


# detect running interactively
if __name__ == '__main__':
    main()

