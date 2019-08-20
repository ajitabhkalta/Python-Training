import threading
import time

def print_even(max_val):
    for i in range(2,max_val,2):
        print(i,end=" ")
        time.sleep(0.3)
    print("")

def print_odd(max_val):
    for i in range(1,max_val,2):
        print(i,end=" ")
        time.sleep(0.3)
    print("")

val = int(input("Enter option 1 or 2:"))
if(val==1):
    start=time.clock()
    print_even(10)
    print_odd(10)
    stop=time.clock()
    print(f"Total time:{stop-start}Secs")
else:
    th1=threading.Thread(target=print_even,name="Thread-1",args=(10,)) #args should be tuple
    th2=threading.Thread(target=print_odd,name="Thread-2",args=(10,))
    start=time.clock()
    th1.start()
    th2.start()
    th1.join() #waits till thread-1 is completed
    th2.join()
    stop=time.clock()
    print(f"Total time with threads:{stop-start}Secs")