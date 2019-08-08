no_of_rows=eval(input("Enter no of rows:"))
print_char = input("Enter char to print in pattern:")
curr_row=1
for row_num in range(no_of_rows,0,-1):
    for _ in range(row_num,0,-1):
        print(print_char,end="")
    for _ in range(1,2*curr_row-1):
        print(" ",end="")
    curr_row+=1
    for _ in range(row_num,0,-1):
        print(print_char,end="")
    print("")
    
gap_row=no_of_rows
for i in range(1,no_of_rows+1):
    print(print_char*i,end="")
    for j in range(1,(2*gap_row-1)):
        print(" ",end="")
    gap_row-=1
    print(print_char*i)