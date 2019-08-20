import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-9s) %(message)s',)

def func():
    logging.debug('thread function running')
    return

if __name__ == '__main__':
    t1 = threading.Timer(5, func)
    t1.setName('t1')
    t2 = threading.Timer(5, func)
    t2.setName('t2')

    logging.debug('starting timers...')
    t1.start()
    t2.start()

    logging.debug('waiting before canceling %s', t2.getName())
    time.sleep(2)
    logging.debug('canceling %s', t2.getName())
    logging.debug('before cancel t2.is_alive() = %d ', t2.is_alive())

    if(t2.is_alive()):
        t2.cancel()
        time.sleep(2)
        logging.debug( 'after cancel t2.is_alive() %d = ', t2.is_alive())

    t1.join()
    t2.join()
    logging.debug('done')