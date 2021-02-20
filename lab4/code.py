import timeit
import random 
import math
import sys

from sorts import *


def timetest_bottomup(runs, n):
    total = 0
    for _ in range(runs):
        thislist = create_random_list(n)
        start = timeit.default_timer()
        mergesort_bottom(thislist)
        end = timeit.default_timer()
        total += end - start
    return total/runs

def timetest_traditional(runs, n):
    total = 0
    for _ in range(runs):
        thislist = create_random_list(n)
        start = timeit.default_timer()
        mergesort(thislist)
        end = timeit.default_timer()
        total += end - start
    return total/runs

#sys.stdout = open("traditional_vs_bottomup_output.txt", "w")
#for i in range(1, 100):
#    print(i*100, timetest_traditional(100, i*100), timetest_bottomup(100, i*100))
#sys.stdout.close()

def test_three_way(thislist):
    return mergesort_three(thislist)

def timetest_three_way(runs, n):
    total = 0
    for _ in range(runs):
        thislist = create_random_list(n)
        start = timeit.default_timer()
        test_three_way(thislist)
        end = timeit.default_timer()
        total += end - start
    return total/runs
    
# for i in range(1, 1000):
#     print(i*100, timetest_three_way(1, i*100))


def test_two_way(thislist):
    return mergesort(thislist)

def timetest_two_way(runs, n):
    total = 0
    for _ in range(runs):
        thislist = create_random_list(n)
        start = timeit.default_timer()
        test_two_way(thislist)
        end = timeit.default_timer()
        total += end - start
    return total/runs
    
# for i in range(1, 1000):
#     print(i*100, timetest_two_way(1, i*100))


def timetest_mergesort_factor(runs, n):
    total = 0
    for _ in range(runs):
        thislist = create_near_sorted_list(runs, n/100)
        start = timeit.default_timer()
        test_two_way(thislist)
        end = timeit.default_timer()
        total += end - start
    return total/runs

# sys.stdout = open("merge_factor_output.txt", "w")
# for i in range(0, 51):
#     print(i, timetest_mergesort_factor(500,i))
# sys.stdout.close()


def timetest_my_quick(runs, n):
    total = 0
    for _ in range(runs):
        thislist = create_random_list(n)
        start = timeit.default_timer()
        my_quicksort(thislist)
        end = timeit.default_timer()
        total += end - start
    return total/runs

def timetest_quicksort_factor(runs, n):
    total = 0
    for _ in range(runs):
        thislist = create_near_sorted_list(runs, n/100)
        start = timeit.default_timer()
        my_quicksort(thislist)
        end = timeit.default_timer()
        total += end - start
    return total/runs

# sys.stdout = open("merge_vs_quick_factor_output.txt", "w")
# for i in range(0, 51):
#     print(i, timetest_mergesort_factor(100, i), timetest_quicksort_factor(100, i))
# sys.stdout.close()
