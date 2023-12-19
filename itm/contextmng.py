# Context managers
# Great tool for resource management allowing you to allocate and release resources precisely as required.


# file management
"""
with open('ctxnotes.txt', 'w') as file:
    file.write('This is a file context manager')


# regular way to manage a file
file = open('ctxnotes.txt', 'w')
try:
    file.write('This is a file operation.')
finally:              # executes with or without an exception
    file.close()

# As can be seen, the "with open" context manager provides a cleaner and more efficient code
"""

# Thread Locking
"""
from threading import Lock
lock = Lock()

lock.acquire()
# do something
lock.release()      # you must say 


# using context manager
with lock:
    # do something
    a = 1
"""

# context manager as a class
"""
class ManagedFile:
    def __init__(self, filename):
        print('init')
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        print('exit')

with ManagedFile('notes.txt') as file:
    print('do some stuff...')
    file.write('some to doo...')

print('continuing...')
"""

# implementing context manager as a function
# using generators and decorators

from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()

with open_managed_file('notesc.txt') as file:
    file.write('someone got this..')
    ''' after exiting the with statement, the function continues to run which then closes the file within the finally clause'''