class Box:
    def __init__( self, len=0, br=0):
       self.length = len
       self.breadth = len
       print(f"Initialized box with length:{len} breadth:{br}")
    def __del__(self):
       class_name = self.__class__.__name__
       print(f"Destroying {class_name} with len ={self.length} br={self.breadth}")
 
 square1 = Box(30,30)
 rectangle = Box(10,30)
 square2 = square1
 print("Deleting Square 1")
 del square1
 print("Deleting Square 2")
 del square2
 print("Deleting rectangle")
 del rectangle
 input()