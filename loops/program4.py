num=int(input("Enter a number:"))
temp=num
res=0
rem=0
while num:
    rem=num%10
    res+=rem
    num=num//10
    if(num==0 and res>9):
        num=res
        res=0
print(f"Sum of digits in {temp} is {res}")