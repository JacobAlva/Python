# DIFFERENCES BETWEEN A PROCESS AND A THREAD

# Process
'''
    A process is an instance of a program (e.g. a Python interpreter)

    A process:
    + Takes advantage of multiple CPUs and cores
    + Utilizes separate memory space -> Memory is not shared between processes
    + Great for CPU-bound processing
    + New process is stated independently from other processes
    + Processes are interruptable/killable
    + One GIL for each process -> avoids GIL limitation

    - Heavyweight
    - Starting a process is slower than starting a thread.
    - More memory
    IPC (inter-process communication) is more complicated
'''