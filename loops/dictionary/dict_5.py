keys="pavan" #keys can be any iterable object
d1=dict.fromkeys(keys)
print(d1)
input()
keys=(1,2,3,4)
values={"hello",10,23,34,45.78,(1,2,34)}
d2=dict.fromkeys(keys,values) #dict.fromkeys(keys,"Default") direct value can be given
print(d2)
input()
l1=[1] #mutable object
d2=dict.fromkeys(keys,l1) #generate dictionary with mutable value
print(d2)
l1.extend("Pavan") #modifying list affects dictionary value too
#l1 contains [1,'p','a','v','a','n']
print(d2) #will contain values with updated list contents
d3=dict.fromkeys(l1,0)
print(d3)
