#Step 1: Define the class
class Point2 :
        #Step 1.1: Declare the method to calculate and return the point's distance from the origin
        def distance_from_origin(self) :
                return (self.__x * self.__x + self.__y * self.__y) ** 0.5
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
p2 = Point2()
p2.set_x(7)
p2.set_y(2)
print("p2 coordinates: (" + str(p2.get_x()) + ", " + str(p2.get_y()) + ")")
print("Distance of p2 from origin = " + str(p2.distance_from_origin()))
