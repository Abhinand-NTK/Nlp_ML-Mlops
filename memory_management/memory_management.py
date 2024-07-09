import gc
class MyObject:

    def __init__(self,name):
        self.name=name
        print(f"Object {self.name} created")

    def __del__(self):
        print(f"Object{self.name} Deleted")

## Create a circular reference

obj1 = MyObject('Obj1')
obj2 = MyObject('Obj2')
obj1.ref=obj2
obj2.ref=obj1

del obj1
del obj2

## Manully Trigger the garbage collector

gc.collect()
print(gc.collect())
print(gc.garbage)

# generator for the memory efficency

def Generate_Numbers(N):
    for i in range(N):
        yield i

# Using generator

for num in Generate_Numbers(10000):
    print(num)
    if num>10:
        break
  

# Profiling the memory usage trace malloc

import tracemalloc

def crate_list():
    return [i for i in range(10000)]

def main():
    tracemalloc.start()
    crate_list()

    snapshot = tracemalloc.take_snapshot()
    top_status = snapshot.statistics('lineno')

    print("[Top 10]")

    print(top_status)

    for stat in top_status[::]:
        print(stat)

main()