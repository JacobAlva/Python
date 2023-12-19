# Context managers
# Great tool for resource management allowing you to allocate and release resources precisely as required.


# file management
with open('ctxnotes.txt', 'w') as file:
    file.write('This is a file context manager')


# regular way to manage a file
file = open('ctxnotes.txt', 'w')
try:
    file.write('This is a file operation.')
finally:              # executes with or without an exception
    file.close()

# As can be seen, the "with open" context manager provides a cleaner and more efficient code