#coding=utf-8
import struct
import random
from heapq import *
import time
limit=100000000
filename="example.dat"
def produceRandomNum():
    f=open(filename,"wb")
    for i in xrange(limit):
        num=random.randint(0,pow(2,20))
        b=struct.pack("i",i)
        f.write(b)
    f.close()


def func():
    now=time.time()
    print("starttime")
    f=open(filename,"rb")
    heapqlst=[]
    for i in range(1000):
        b=f.read(4)
        num=struct.unpack('i',b)
        heappush(heapqlst,num)
    
    f.seek(4000)
    while True:
        b=f.read(4)
        if not b:
            break
        num=struct.unpack('i',b)
        if num<=heapqlst:
            continue
        heapreplace(heapqlst,num)
    f.close()
    end=time.time()
    runtime=end-now
    print("%d"%heapqlst[0])
    print("runtime:%d"%runtime)

#produceRandomNum()
func()


