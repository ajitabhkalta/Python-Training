rows = int(input("Enter no of rows:"))
x=input("Enter char to print in pattern:")

for i in range(1,rows+1):
    for _ in range(1,rows):
        print(x,end=" ")
    print("")    