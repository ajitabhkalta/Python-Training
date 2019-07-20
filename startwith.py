x=input("Enter any string:")
y=input("Enter substring to search:")
if (x.startswith(y)):
    print(f"{x} starts with {y}")
else:
    print(f"{x} doesn't start with {y}")
if(x.endswith(y)):
    print(f"{x} ends with {y}")
else:
    print(f"{x} doesn't end with {y}")

#startswith(str,beg,end)
print(x.startswith(y,2,5))
input()
#find returns index of sub string if found else -1 if not found
x=input("Enter any string:")
y=input("Enter substring to search:")
print(x.find(y))
print(x.find(y,3,8))