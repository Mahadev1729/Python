## multithreading
## I/O bound tasks:

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2) ## wait for 2 unit of time
        print(f"number:{i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter:{letter}")
        
## create 2 threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letter)        
t=time.time()
# print_numbers()
# print_letter()
## start the thread
t1.start()
t2.start()
## wait for 
t1.join()
t2.join()

finished_time=time.time()-t
print(finished_time)

