num=int(input("Enter any number:"))
pos = int(input("Enter bit position:"))
print(f"Bin equivalent of given number {num} is",bin(num))
x= num| (1<<(pos-1))
print(f"Val after setting bit at position {pos} in number {num} is",x )
print(f"Bin equivalent is",bin(x))
x =num & (~(1<<(pos-1)))
print(f"Val after clearing bit at position {pos} in number {num} is",x )
print(f"Bin equivalent is",bin(x))
x = num ^ (1<<(pos-1))
print(f"Val after toggling bit at position {pos} in number {num} is",x )
print(f"Bin equivalent is",bin(x))