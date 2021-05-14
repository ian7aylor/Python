'''
class BaseClass:
  Body of base class
class DerivedClass(BaseClass):
  Body of derived class
  '''

# parent class
#Methods are functions inside class
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()      #runs parent init function
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()       
peggy.whoisThis()
peggy.swim()
peggy.run()

#Encapsulation
class Computer:

    def __init__(self):
        self.__maxprice = 900       #Initialize instance attribute

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))  #Prints max price

    def setMaxPrice(self, price):
        self.__maxprice = price     

c = Computer()
c.sell()    #initialize instance

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()

#Example of inheritance
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]    #Starts at 0

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
            
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)
        
