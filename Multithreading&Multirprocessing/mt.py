#Multithreading
#What is the importence :- IO kind of operations
#By performing multliple operations

import threading
import time

def print_numbers():

    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")
    
def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter:{letter}")


## Create two threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letter)

t = time.time()
t1.start()
t2.start()

t1.join()
t2.join()
# print_numbers()
# print_letter()
finished_time = time.time()-t
print(finished_time)