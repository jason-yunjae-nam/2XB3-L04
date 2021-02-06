import timeit
import random 
import math
import sys

from sorts import *

def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L


def create_near_sorted_list(n, factor):
    L = create_random_list(n)
    L.sort()
    for _ in range(math.ceil(n*factor)):
        index1 = random.randint(0, n-1)
        index2 = random.randint(0, n-1)
        L[index1], L[index2] = L[index2], L[index1]
    return L

def test_inplace(thislist):
    return quicksort_inplace(thislist)

def timetest_inplace(runs, n):
    total = 0
    for _ in range(runs):
        thislist = create_random_list(n)
        start = timeit.default_timer()
        test_inplace(thislist)
        end = timeit.default_timer()
        total += end - start
    return total/runs
    
#sys.stdout = open("inplace_output.txt", "w")
# for i in range(1, 100):
#     print(i*100, timetest_inplace(100, i*100))
#sys.stdout.close()

def test_my_quick(thislist):
    return my_quicksort(thislist)

def timetest_my_quick(runs, n):
    total = 0
    for _ in range(runs):
        thislist = create_random_list(n)
        start = timeit.default_timer()
        test_my_quick(thislist)
        end = timeit.default_timer()
        total += end - start
    return total/runs

# # sys.stdout = open("my_quick_output.txt", "w")
# for i in range(1, 500):
#     print(i*10, timetest_my_quick(100, i*10))
# sys.stdout.close()

def test_dual(thislist):
    return dual_pivot_quicksort(thislist)

def timetest_dual(runs, n):
    total = 0
    for _ in range(runs):
        thislist = create_random_list(n)
        start = timeit.default_timer()
        test_dual(thislist)
        end = timeit.default_timer()
        total += end - start
    return total/runs

# sys.stdout = open("dual_output.txt", "w")
# for i in range(1, 500):
#     print(i*10, timetest_dual(100, i*10))
# sys.stdout.close()

def test_tri(thislist):
    return tri_pivot_quicksort(thislist)

def timetest_tri(runs, n):
    total = 0
    for _ in range(runs):
        thislist = create_random_list(n)
        start = timeit.default_timer()
        test_tri(thislist)
        end = timeit.default_timer()
        total += end - start
    return total/runs

# sys.stdout = open("tri_output.txt", "w")
# for i in range(1, 500):
#     print(i*10, timetest_tri(100, i*10))
# sys.stdout.close()

def test_quad(thislist):
    return quad_pivot_quicksort(thislist)

def timetest_quad(runs, n):
    total = 0
    for _ in range(runs):
        thislist = create_random_list(n)
        start = timeit.default_timer()
        test_quad(thislist)
        end = timeit.default_timer()
        total += end - start
    return total/runs

# sys.stdout = open("quad_output.txt", "w")
#for i in range(1, 500):
#    print(i*10, timetest_quad(100, i*10))
# sys.stdout.close()


def timetest_dual_factor(runs, n):
    total = 0
    for _ in range(runs):
        thislist = create_near_sorted_list(1000, n/100)
        start = timeit.default_timer()
        test_dual(thislist)
        end = timeit.default_timer()
        total += end - start
    return total/runs


def test_bubble(thislist):
    return bubble_sort(thislist)

def timetest_bubble_factor(runs, n):
    total = 0
    for _ in range(runs):
        thislist = create_near_sorted_list(1000, n/100)
        start = timeit.default_timer()
        test_bubble(thislist)
        end = timeit.default_timer()
        total += end - start
    return total/runs


def test_selection(thislist):
    return selection_sort(thislist)

def timetest_selection_factor(runs, n):
    total = 0
    for _ in range(runs):
        thislist = create_near_sorted_list(1000, n/100)
        start = timeit.default_timer()
        test_selection(thislist)
        end = timeit.default_timer()
        total += end - start
    return total/runs


def test_insertion(thislist):
    return insertion_sort(thislist)

def timetest_insertion_factor(runs, n):
    total = 0
    for _ in range(runs):
        thislist = create_near_sorted_list(1000, n/100)
        start = timeit.default_timer()
        test_insertion(thislist)
        end = timeit.default_timer()
        total += end - start
    return total/runs

#sys.stdout = open("dualoutput.txt", "w")
#for i in range(1, 100):
#    print(i, timetest_dual_factor(10,i), timetest_bubble_factor(10,i), timetest_selection_factor(10,i), timetest_insertion_factor(10,i))
#sys.stdout.close()

def timetest_insertion(runs, n):
    total = 0
    for _ in range(runs):
        thislist = create_random_list(n)
        start = timeit.default_timer()
        test_insertion(thislist)
        end = timeit.default_timer()
        total += end - start
    return total/runs

def test_final(thislist):
    return final_sort(thislist)

def timetest_final(runs, n):
    total = 0
    for _ in range(runs):
        thislist = create_random_list(n)
        start = timeit.default_timer()
        test_final(thislist)
        end = timeit.default_timer()
        total += end - start
    return total/runs

sys.stdout = open("dualoutput.txt", "w")
for i in range(1, 1000):
    print(i, timetest_final(10,i), timetest_dual(10,i), timetest_insertion(10,i))
sys.stdout.close()