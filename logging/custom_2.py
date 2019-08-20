import logging
from random import choice

logging.basicConfig(level=logging.WARNING,format='%(asctime)s %(process)s %(funcName)s - %(message)s ')
#datefmt="%Y-%m-%d %H:%M:%S" can be changed to your wish
def handle_exception1():
    print("Using exception method")
    logging.exception("Exception Occured")

def handle_exception2():
    print("Using error method")
    logging.error("Exception occurred", exc_info=True)

l=[1,2,3,4]

func_list=[handle_exception1,handle_exception2]
def access_list():
    try:
        print(l[10])
    except Exception:
        choice(func_list)()
    
access_list()