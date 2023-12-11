# DIFFERENCES BETWEEN A PROCESS AND A THREAD

''' # Process
    A process is an instance of a program (e.g. a Python interpreter)

    A process:
    + Takes advantage of multiple CPUs and cores
    + Utilizes separate memory space -> Memory is not shared between processes
    + Great for CPU-bound processing
    + New process is stated independently from other processes
    + Processes are interruptable/killable
    + One GIL for each process -> avoids GIL limitation (Global interpreter lock)

    - Heavyweight
    - Starting a process is slower than starting a thread.
    - More memory
    IPC (inter-process communication) is more complicated
'''

''' # Threads
    A thread is an entity within a process that can be scheduled (also known as leightweight process). A process can have multiple threads within it.

    + All threads within a process share the same memory
    + Leightweight
    + Starting a thread is faster than starting a process
    + Great for I/O bound tasks

    - Threading is limited by GIL: only one thread at a time
    - No effect for CPU bound tasks
    - Not interruptable/killable
    - Careful with race conditions - since threads share the same memory, multiple threads might want to modify the content of the memory simultaneously.
'''

''' # GIL - Global Interpreter Lock
    - GIL is a lock that allows only one thread at a time to execute in Python.
    - Needed in CPython because memory management is not thread-safe.   #Avoid CPython, not safe.

    - Avoid:
        - Use multiprocessing
        - Use a different, free-threaded Python implementation (Jython, IronPython)
        - Use Python as a wrapper for third-party libraries (C/C++) -> numpy, scipy
'''


from multiprocessing import Process, Value, Array, Lock
import os
import time

"""
def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

    
processes = []
num_processes = os.cpu_count()
print(f'The number of CPUs are {num_processes}')
# create processes
for i in range(num_processes):
    p = Process(target=square_numbers)
    processes.append(p)

# start 
for p in processes:
    p.start()

# join
for p in processes:
    p.join()

print('End main')


from threading import Thread

def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)

    
threads = []
num_threads = 10

# create threads
for i in range(num_threads):
    t = Thread(target=square_numbers)
    threads.append(t)

# start 
for t in threads:
    t.start()

# join
for t in threads:
    t.join()

print('End main')
"""

'''----------------------------------------------------------'''

# Multiprocessing

""" multp
def square_numbers():
    for i in range(1000):
        i * i

if __name__ == "__main__":
    processes = []
    num_processes = os.cpu_count()      # returns the num of CPUs on the machine. Usually a good choise for the number of processes.
    print(f'The number of CPUs are {num_processes}')


    # create processes and assign a function for each process
    for i in range(num_processes):
        proc = Process(target=square_numbers)
        processes.append(proc)

    # start all processes
    for proc in processes:
        proc.start()

    # wait for all processes to finish
    # block the main program until these processes are finished
    for proc in processes:
        proc.join()
"""

# sharing data between processes
'''
    While data can be shared easily between threads with a global variable as multiple threads within the same process reference the same memory, processes however don't leave in the same memory space and thus, don't have access to the same data. 
    There are two shared memory objects that can be used to share data between processes, Values and Arrays.
'''

# sharing a single value between processes
"""
def add_100(number, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            number.value += 1

if __name__ == "__main__":

    lock = Lock()
    shared_number = Value('i', 0)
    print('Number at beginning is', shared_number.value)

    p1 = Process(target=add_100, args=(shared_number,lock))
    p2 = Process(target=add_100(shared_number,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('number at end is', shared_number.value)
    # if the output at this point is not 200, then a race conditon has occurred due to multiple processes accessing/modifying the shared variable (number.value) simultaneously. To prevent this, we must use a Lock.
"""

# sharing an array with multiple processes
def add_100(numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            for i in range(len(numbers)):
                numbers[i] += 1
        

if __name__ == "__main__":

    lock = Lock()
    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('Array at beginning is', shared_array[:])

    p1 = Process(target=add_100, args=(shared_array,lock))
    p2 = Process(target=add_100(shared_array,lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Array at end is', shared_array[:])