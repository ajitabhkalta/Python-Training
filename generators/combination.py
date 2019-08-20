def combinations(val):
    for char in val:
        for curr_pos in range(len(val)):
            if val[curr_pos] != char:
                yield(char+val[curr_pos]) #AB AC AD etc

val=input("Enter any string:")
gen_func=combinations(val)
#method 1
for i in gen_func:
    print(i,end=" ")
print("")
#for loop code internally implemented as 
gen_func=combinations(val)
while True:
    try:
        i = next(gen_func)
        print(i)
    except StopIteration:
        print("stop iteratio received")
        break
# Reset generator back to start 
gen_func=combinations(val)
print(next(gen_func))
print(next(gen_func))
print(next(gen_func))
print(next(gen_func))