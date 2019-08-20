import threading 
  
# global variable x 
x = 0
  
def increment(): 
    global x 
    x += 1
  
def thread_task(lock): 
    t = threading.currentThread()
    print(t.getName())
    lock.acquire()
    for _ in range(100000): 
        increment() 
    lock.release() 
  
def main_task(): 
    global x 
    x = 0
  
    # creating a lock 
    lock = threading.Lock() 
  
    # creating threads 
    t1 = threading.Thread(target=thread_task, args=(lock,)) 
    t2 = threading.Thread(target=thread_task, args=(lock,)) 
  
    # start threads 
    t1.start() 
    t2.start() 
  
    # wait until threads finish their job 
    t1.join() 
    t2.join() 
  
if __name__ == "__main__": 
    t = threading.currentThread()
    print(t.getName())
    for i in range(10): 
        main_task() 
        print(f"Iteration {i+1}: x = {x}") 