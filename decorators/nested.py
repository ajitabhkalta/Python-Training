import functools

def print_twice(func):
    @functools.wraps(func)
    def inner(*args):
        "Inner decorator function"
        func(*args)
        func(*args)
    return inner

@print_twice
def print_mesg(mesg):
    "Prints a message"
    print(mesg)

#drvr code
mesg=input("Enter any message:")
print_mesg(mesg)
print("Name of function:",print_mesg.__name__)
help(print_mesg)