inp1=input("Enter your name:")
print(type(inp1))
inp2=input("Enter your age:")
print(type(inp2))
print("Hi",inp1,"Your age in days is:",(inp2*365))

#To avoid having input as always string
#Type conversion
#Using eval

#Using type conversion
inp1=input("Enter your name:")
print(type(inp1))
inp2=int(input("Enter your age:"))
print(type(inp2))
print("Hi",inp1,"Your age in days is:",(inp2*365))


#using eval
inp1=input("Enter your name:")
print(type(inp1))
inp2=eval(input("Enter your age:"))
print(type(inp2))
print("Hi",inp1,"Your age in days is:",(inp2*365))
