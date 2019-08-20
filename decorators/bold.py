def make_italic(func):
    def inner(*args):        
        return "<I>"+func(*args)+"</I>"
    return inner

def make_bold(func):
    def inner(*args):        
        return "<B>"+func(*args)+"</B>"
    return inner

data=input("Enter message:")
@make_bold
@make_italic
def print_html_data(data):
    return data
print(print_html_data(data))

    