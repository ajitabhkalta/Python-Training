#Basic iterator
l1=["Orange","Papaya","Apple","Banana"]
x=iter(l1)
print(x)
print(type(x))
l2=("Orange","Papaya","Apple","Banana")
y=iter(l2)
print(y)
print(type(y))
while True:
    try:
        print(next(x)) #will give me one element at a time
    except StopIteration:
        print("Items empty")
        break