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


from multiprocessing import Process
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
"""

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