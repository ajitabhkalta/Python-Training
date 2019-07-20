#Program to show else with while
num = int(input("Enter a number:"))
while num>0:
    if(num == 5): #if break is executed and loop is broken else will never be executed
        break
    print(f"{num}",end=" ")
    num-=1
else:
    print("LOOP COMPLETED SUCCESFULLY")