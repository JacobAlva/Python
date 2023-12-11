# sharing data between threads

from threading import Thread, Lock, current_thread
import time
from queue import Queue

"""
def square_numbers():
    for i in range(100):
        i * i

if __name__ == "__main__":
    threads = []
    num_threads = 10

    # create threads
    for i in range(num_threads):
        thread = Thread(target=square_numbers)
        threads.append(thread)

    # start threads
    for thread in threads:
        thread.start()

    # join threads: wait for them to complete
    for thread in threads:
        thread.join()

    print('end main')


# sharing data between threads

database_value = 0

def increase(lock):
    global database_value
    
    lock.acquire()                  # allows the thread to lock the state (database_value) and prevent another thread from simultaneously modifying it (race condition)
    local_copy = database_value
    #processing
    local_copy += 1
    time.sleep(0.1)     # allows the program to switch to the other thread. This should be prevented by using locks.
    database_value = local_copy
    lock.release()                  # everytime you acquire a lock, always release it.

    # alternatively
    with lock:
        local_copy = database_value
        local_copy += 1
        time.sleep(0.1)    
        database_value = local_copy


if __name__ == "__main__":

    lock = Lock()
    print('start value', database_value)

    thread1 = Thread(target = increase, args=(lock,))  # the lock prevents another thread from... ## the trailing comma is to tell Python this is a single element tuple
    thread2 = Thread(target = increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('end value', database_value)
    print('end main')


# working with queues
if __name__ == '__main__':

    q = Queue()

    q.put(1)
    q.put(2)
    q.put(3)

    # 3 2 1 >
    first = q.get()
    print(first)

    q.task_done()       # tells the program we're done processing the queue
    q.join()            # blocks the main thread until all elements in queue are processed.
    q.empty()           # returns True if queue is empty

    print('end main')
"""

# queue use case

def worker(q, lock):
    while True:
        value = q.get()
        #processing
        with lock:
            print(f'in {current_thread().name} got {value}')
        q.task_done()


if __name__ == "__main__":

    q = Queue()
    lock = Lock()
    num_threads = 10

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        thread.daemon=True          # this is a background thread that will die when the main thread dies. this helps to exit the while loop above.
                                    # thread.daemon=False by default and we would need some statement e.g. "if (some condition): break" to exit the loop
        thread.start()
    
    for i in range(1, 21):
        q.put(i)
    
    q.join()
    print('end main')