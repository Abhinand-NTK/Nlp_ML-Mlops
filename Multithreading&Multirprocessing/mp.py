#Multiprocessing
#Process that run in parallel 
# When to use the multiprocessing : Using the cpu bound tasks
# Parallell Exection - Multiple cores of the CPU

import multiprocessing
import multiprocessing.process
import time


def square_numbers():

    for i in range(5):
        time.sleep(1)
        print(f"Square{i*i}")


def cube_numbers():

    for i in range(5):
        time.sleep(1)
        print(f"Cube{i*i*i}")


if __name__=="__main__":


    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)

    t=time.time()

    ## Start the process
    p1.start()
    p2.start()

    ## Wait for the process to complete

    p1.join()
    p2.join()
    
    finished_time = time.time()-t
    print(finished_time)
