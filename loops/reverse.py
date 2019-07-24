num=int(input("Enter any number:"))
temp=num
result=0
while num:
    rem=num%10
    result=(result*10)+rem
    num//=10
    print(f"Reverse of given num{temp} is {result}")