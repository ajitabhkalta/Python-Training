x=[] 
print(x)

for _ in range(4):
    x.append(eval(input("Enter any data:")))

print(x)
input()
val=int(input("Enter index num to del data inside a list:"))
if val>len(x):
    print("Invalid index")
else:
    del x[val-1]
    print("After deleting list contains:",x)
input()
del x
print("Accesing list after del...")
print(x) 