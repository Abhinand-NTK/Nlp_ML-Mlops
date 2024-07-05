'''
Real world exmple: Multiprocessing for CPU-bounds
Scenrio : Factorial Calclation
Factorial calculation,especually for larage numbers
invloves significant computentnal work
'''

import multiprocessing
import math
import multiprocessing.pool
import sys
import time

sys.set_int_max_str_digits(100000)
#funciton to compute the factorial of the given number
def compute_my_factorial(Number):
    print(f"factorial of the {Number}")
    result=math.factorial(Number)
    print(f"factorail of the {Number} is {result}")
    return result
if __name__ == "__main__":
    numbers=[1000,2000,3000,4000]
    start_time = time.time()

    with multiprocessing.Pool() as pool:
        results=pool.map(complex,numbers)

    end_time =time.time()

    print(f"Results:{results}")
    print(f"Time taken:{end_time-start_time} seconds")
