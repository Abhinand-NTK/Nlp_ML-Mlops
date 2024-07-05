import sys
a = []
print(sys.getrefcount(a))
b=a
print(sys.getrefcount(b))
del b
print(sys.getrefcount(a))

## Garbage Collection

import gc

gc.enable()
gc.disable()
print(gc.collect())

#get Garbage collection statics

print(gc.get_stats())

## Get unreachable objects

print(gc.garbage)
