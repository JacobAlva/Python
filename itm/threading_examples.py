# sharing data between threads

from threading import Thread, Lock
import time

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
"""

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

    thread1 = Thread(target = increase, args=(lock,))  # the lock prevents another thread from...
    thread2 = Thread(target = increase, args=(lock,))       # this also works > increase(lock)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('end value', database_value)
    print('end main')