#identity check can be done on any data type
x = eval(input("enter 1st num:"))
y = eval(input("enter 2nd num:"))
#"is" returns True if two values have 
# same identity
#"is not" return True if two values have 
# different identity
if x is y:
    print(f"{x} has same identity as {y}")
else:
    print(f"{x} is at {hex(id(x))} {y} is at {hex(id(y))}")