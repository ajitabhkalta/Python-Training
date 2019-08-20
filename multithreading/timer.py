import threading
import time
import logging
import random

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(asctime)s %(message)s',)

def random_sleep():
    t = threading.currentThread()
    print(t.getName())
    r = random.randint(1,10)
    logging.debug('sleeping %s sec', r)
    time.sleep(r)
    logging.debug('ending')
    return

if __name__ == '__main__':
    for i in range(3):
        t = threading.Thread(target=random_sleep,name=f"thread{i+1}")
        t.setDaemon(True)
        t.start()

    main_thread = threading.current_thread()
    print(threading.enumerate())
    for t in threading.enumerate():
	    if t is main_thread:
		    continue
	    logging.debug('joining %s', t.getName())
	    t.join()