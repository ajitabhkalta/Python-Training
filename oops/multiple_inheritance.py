class Person():  
    def __init__(self, personName, personAge):  
        self.name = personName  
        self.age = personAge  

    def showPersonInfo(self):  
        print(f"Name:{self.name}\nAge:{self.age}")  
   
class Student():
    def __init__(self, studentId, doj):  
        self.studentId = studentId  
        self.doj = doj
 
class Animation(Student, Person): # extends both Person and Student class  
    def __init__(self, name, age, id, doj):  
        Person.__init__(self, name, age)  
        Student.__init__(self, id, doj) 
    def studentInfo(self):
        super().showPersonInfo()
        print(f"Batch:{self.__class__.__name__}\nId:{self.studentId}\nDOJ:{self.doj}")
  
# Create an object of the Animation  
std1 = Animation('Suresh', 30, '102',"2/10/2018")  
std1.studentInfo()
std2 = Animation('Anitha', 24, '103',"2/10/2019")  
std2.studentInfo()
