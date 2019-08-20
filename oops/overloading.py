import math
class Circle:
 
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def area(self):
        return math.pi * self.radius ** 2
    #__radd__
    def __radd__(self,data):
        return Circle( self.radius + data )

    def __add__(self, another_circle):
        if(isinstance(another_circle,type(self))):
            return Circle( self.radius + another_circle.radius )
        elif(isinstance(another_circle,(int,float))):
            return Circle( self.radius + another_circle)
        else:
            print("Invalid data provided")
 
    def __gt__(self, another_circle):
        return self.radius > another_circle.radius
 
    def __lt__(self, another_circle):
        return self.radius < another_circle.radius

 
c1 = Circle(4)
print("c1\n\tradius:",c1.getRadius())
print("\tArea:",c1.area())
c2 = Circle(5)
print("c2\n\tradius:",c2.getRadius())
print("\tArea:",c2.area())
c3 = c1 + c2
print("c3\n\tradius:",c3.getRadius())
print("\tArea:",c3.area())

c4 = 20 + c2
print("c4\n\tradius:",c4.getRadius())
print("\tArea:",c4.area())

c5 = c2 + 40
print("c5\n\tradius:",c5.getRadius())
print("\tArea:",c5.area())

print(c1>c2)
print(c1<c3)