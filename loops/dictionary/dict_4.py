d1={"Name":"pavan","age":33,"Place":"Bangalore"}
print(d1.get("Salary"))
print(d1.get("Salary","Oops!Data not found")) #user can provide value of his choice
print(d1.get("Name","Data not found")) #prints valid data if 
print({"Name":"pavan","age":33,"Place":"Bangalore"}.get("age"))
d1.clear()#flush all the data in dictionary d1->{}
print(d1)
del d1
print(d1) #NameError