d1={1:"Hello",2:"Bye",3:"Hurray",4:"Alas"}
print(d1.keys())
input()
#print only keys
for k in d1.keys():
    print(k)
input()
#print only values
print(d1.values())
input()
for v in d1.values():
    print(v)
input()
#fetch items (both key and value)
print(d1.items())
for k,v in d1.items():
    print(k,v)
input()
# #fetching each key from a tuple
d1={(1,2,3):"Hello",2:"Bye",3:"Hurray",4:"Alas"}
for k,v in d1.items():
    if(type(k) == tuple):
        for l in k:
            print(l)
        print(v)
    else:
        print(k,v)