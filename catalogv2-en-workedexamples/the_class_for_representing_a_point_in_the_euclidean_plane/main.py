#Step 1: Define the class
class Point1 :
        #Step 1.1: Declare the method to shift the location of the point by the given amount
        def translate(self, dx, dy) :
                self.__x += dx
                self.__y += dy
        #Step 1.2: Define the setter and getter methods for the x-coordinate of the point
        def set_x(self, new_x) :
                self.__x = new_x
        def get_x(self) :
                return self.__x
        #Step 1.3: Define the setter and getter methods for the y-coordinate of the point
        def set_y(self, new_y) :
                self.__y = new_y
        def get_y(self) :
                return self.__y
#Step 2: Test the class
p1 = Point1()
p1.set_x(7)
p1.set_y(2)
p1.translate(11, 6)
print("p1 coordinates: (" + str(p1.get_x()) + ", " + str(p1.get_y()) + ")")
