l1=["apple","banana","mango","apple","Grapes","banana"]
l2=[[1,10,10,20,30],[4,6,8]]
print(l1.count("apple"))
print(l1.index("banana")) #prints first index matched in the list
print(l1.index("banana",l1.index("banana")+1))
input()
#ind=l1.index("orange") #reports ValueError
l1.sort() #sort in ascending
print(l1)
l1.sort(reverse=True) #descending order sorting
print(l1)
l2.sort(reverse=True)
print(l2)
0