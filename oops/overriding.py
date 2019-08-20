class Employee:
    salary=10000
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def employeeLevel(self):
        print("Level-1")

    def getSalary(self):
        return Employee.salary

class Engineer(Employee):
    def __init__(self,name,age,dept,sal):
        super().__init__(name,age)
        if(sal<super().getSalary()):
            self.sal=super().getSalary()
        else:
            self.sal=sal
    def getSalary(self):
        return self.sal

    def employeeLevel(self,level):
        print(level)

e1=Engineer("pavan",33,"DEV",8000)
e2=Engineer("kumar",38,"QA",12000)
e3=Engineer("mahesh",38,"QA",15000)

