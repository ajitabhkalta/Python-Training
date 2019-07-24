val = abs(int(input("Enter any value:")))
for i in range(1,val):
    print(f"{i} ",end="")
#odd nums
print("\nodd-numbers")
for i in range(1,val,2):
    print(f"{i} ",end="")
#even nums
print("\neven-numbers")
for i in range(2,val,2):
    print(f"{i} ",end="")
#negative num
print("\nNegative-numbers")
for i in range(-1,-val,-1):
    print(f"{i} ",end="")