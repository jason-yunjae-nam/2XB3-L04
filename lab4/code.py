#testing goes here :)
import timeit
import random 
import math
import sys

from sorts import *

def test_inplace(thislist):
    return quicksort_inplace(thislist)

def timetest_bottomup(runs, n):
    total = 0
    for _ in range(runs):
        thislist = create_random_list(n)
        start = timeit.default_timer()
        mergesort_bottom(thislist)
        end = timeit.default_timer()
        total += end - start
    return total/runs
    
#sys.stdout = open("bottomup_output.txt", "w")
#for i in range(1, 100):
#    print(i*100, timetest_bottomup(100, i*100))
#sys.stdout.close()

def timetest_traditional(runs, n):
    total = 0
    for _ in range(runs):
        thislist = create_random_list(n)
        start = timeit.default_timer()
        mergesort(thislist)
        end = timeit.default_timer()
        total += end - start
    return total/runs

#sys.stdout = open("traditional_output.txt", "w")
for i in range(1, 100):
    print(i*100, timetest_traditional(100, i*100), timetest_bottomup(100, i*100))
#sys.stdout.close()