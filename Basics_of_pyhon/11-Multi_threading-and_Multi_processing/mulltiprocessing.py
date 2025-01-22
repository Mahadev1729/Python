##processing that run parallel
## CPU_bound tasks-tasks that are heavy on cpu usage(e.g:mathamatical computation)
##Paralle execution-Multiple cores of the cpu

import mulltiprocessing

import time

def square_number():
    for i in range(5):
        time.sleep(1)
        print(f"{i} Square:{i*i}")

def cube_number():
    for i in range(5):
        time.sleep(1.5)
        print(f"{i} cube:{i*i*i}")
        
if __name__=="__main__":# entry point
# square_number()
# cube_number()
## create two process
    pl=mulltiprocessing.Process(target=square_number)
    p2=mulltiprocessing.Process(target=cube_number)

    t1=time.time()

    pl.start()
    p2.start()

    p1.join()
    p2.join()

    finished_time=time.time()-target
    print(finished_time)
