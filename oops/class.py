#class demo
#object which is parent for every orphan class
class Book():
    "Holds books info"
    book_count=0    #class attribute 
    def __init__(self,title,price,num_books): #with no parameters __init__ is called non parameterized constructor
        self.title=title #instance attribute
        self.price=price
        self.book_count = num_books
        Book.book_count+=num_books #class attribute

    def printbookinfo(self):
        print(f"Book-Details\nName:{self.title}\n\tQuantity:{self.book_count}\n\tPrice:{self.price}")

print(Book.__doc__) #prints doc string written in class
help(Book)

while True:
    name=input("Enter book name:")
    if not name:
        break
    price=float(input("Enter book price:"))
    num_books=int(input("Enter number of books:"))
    
    b1=Book(name,price,num_books)
    b1.printbookinfo() #method 1
    # Book.printbookinfo(b1) #method 2
    print(f"Total number of books:{Book.book_count}")






