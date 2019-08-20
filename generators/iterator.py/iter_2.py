class MyRange():
    def __init__(self, start, stop=0):
        if stop == 0:
            self.high = start
            self.current = 0
        else:
            self.high = stop
            self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.high:
            #print("Raising stop iteration")
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1
#1st method
num_iter = MyRange(1,10)    
print(list(num_iter))
input()
#2nd method
num_iter = MyRange(6) 
for i in num_iter:
    print(i,end=" ")
print("") #just to introduce new line
input()
for i in MyRange(20,50):
    print(i,end=" ")
input()
num_iter=MyRange(3)
print("") #just to introduce new line
#3rd method
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))
print(next(num_iter))