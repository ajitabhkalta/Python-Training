name=input("Enter name:")
g = input("Enter gender M/F:")
age = eval(input("Enter age:"))

if(((g == "M") or (g == "m")) and (age >=21)):
    print(f"{name} is eligible to get married")

elif(((g == "F") or (g == "f")) and (age >=18)):
    print(f"{name} is eligible to get married")
    
else: #else is not mandatory
    print(f"{name} with gender {g} not eligible to get married")
