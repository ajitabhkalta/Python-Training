#simple decorator
def my_decorator(func):
    def gift_wrapper():
        print("Wrapped Gift with cover")
        func()
        print("Message written: \"Happy Birthday sweet heart :)\"")
    return gift_wrapper

def gift():
    print("\u25C8%5s\u25C8\n%1s\u25C8%3s\u25C8\n%2s\u25C8%1s\u25C8\n%3s\u25C8"\
          %("","","","","",""))

wife = my_decorator(gift)
print(wife)
wife()