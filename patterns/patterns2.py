import time
rows = int(input("Enter no of rows:"))
x=input("Enter char to print in pattern")
gap_row=rows
for i in range(1,rows+1):
    print(x*i,end="")
    for j in range(1,(2*gap_row-1)): #2*5-1=9,2*4-1.2*3-1,2*2-1
        print(" ",end="")
    gap_row-=1
    print(x*i)
    time.sleep(1)