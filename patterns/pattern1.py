rows = int(input("Enter no of rows:"))
x=input("Enter char to print in pattern:")
#with space
for i in range(1,rows+1):
    for _ in range(1,i+1):
        print(x,end=" ")
    print("")    