my_list=[]
x=eval(input("enter the range of number:"))
for i in range(1,x+1):
    my_list.append(i)
print(my_list)
result=1
for item in my_list:
    result=result*item
print("multiplication of all elements:",result)