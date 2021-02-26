import timeit
import random 
import math
import sys

from heap import *

def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L

def timetest_build_heap1(runs, n):
    total = 0
    for _ in range(runs):
        thislist = create_random_list(n)
        thisheap = Heap(thislist)
        start = timeit.default_timer()
        thisheap.build_heap1()
        end = timeit.default_timer()
        total += end - start
    return total/runs

def timetest_build_heap2(runs, n):
    total = 0
    for _ in range(runs):
        thislist = create_random_list(n)
        thisheap = Heap(thislist)
        start = timeit.default_timer()
        thisheap.build_heap2()
        end = timeit.default_timer()
        total += end - start
    return total/runs

def timetest_build_heap3(runs, n):
    total = 0
    for _ in range(runs):
        thislist = create_random_list(n)
        thisheap = Heap(thislist)
        start = timeit.default_timer()
        thisheap.build_heap3()
        end = timeit.default_timer()
        total += end - start
    return total/runs

#sys.stdout = open("build_heap_1_2_3.txt", "w")
for i in range(1, 100):
    print(i, timetest_build_heap1(10, i), timetest_build_heap2(10, i), timetest_build_heap3(10, i))
#sys.stdout.close()