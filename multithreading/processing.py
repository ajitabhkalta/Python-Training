import multiprocessing 
import time
import os
  
def print_even(max_val):
    for i in range(2,max_val,2):
        print(i,end=" ")
        time.sleep(5)
    print("")

def print_odd(max_val):
    for i in range(1,max_val,2):
        print(i,end=" ")
        time.sleep(5)
    print("")

  
if __name__ == "__main__": 
    print(f"Id of current process is {os.getpid()}")
    # creating processes 
    p1 = multiprocessing.Process(target=print_even, args=(10, )) 
    p2 = multiprocessing.Process(target=print_odd, args=(10, )) 
  
    # starting process 1 
    p1.start() 
    # starting process 2 
    p2.start() 
  
    # process IDs 
    print("ID of process p1: {}".format(p1.pid)) 
    print("ID of process p2: {}".format(p2.pid)) 
    # wait until process 1 is finished 
    p1.join() 
    # wait until process 2 is finished 
    p2.join() 
  
    # both processes finished 
    print("Done!") 