import timeit
import sys

# testing runtime of copy() function

def test_list_copy(thislist, n):
    return thislist.copy()

def timetest_copy(runs, n):
    total = 0
    thislist = list(range(1,n))
    for _ in range(runs):
        start = timeit.default_timer()
        test_list_copy(thislist, n)
        end = timeit.default_timer()
        total += end - start
    return total/runs

'''
for i in range(1, 1000):
    print(i*100, timetest_copy(100, i*100))'''


# testing runtime of lookup() function

def test_list_lookup(thislist, i):
    return thislist[i]

def timetest_lookup(thislist, i):
    start = timeit.default_timer()
    test_list_lookup(thislist, i)
    end = timeit.default_timer()
    return end - start

'''
thislist = list(range(1000000))
sys.stdout = open("lookup_output.txt", "w")
for i in range(len(thislist)):
    print(i, timetest_lookup(thislist, i))
sys.stdout.close()'''


# version 2 test of lookup() function

def lookup_2(thislist, i):
    return thislist[i]

def timetest_lookup_2(runs, thislist, i):
    total = 0
    for _ in range(runs):
        start = timeit.default_timer()
        lookup_2(thislist, i)
        end = timeit.default_timer()
        total += end - start
    return total/runs

'''
thislist = list(range(1000000))
sys.stdout = open("lookup2_output.txt", "w")
for i in range(len(thislist)):
    print(i, timetest_lookup_2(100, thislist, i))
sys.stdout.close()'''


# testing runtime of append() function

def test_list_append(thislist, i):
    return thislist.append(i)

def timetest_append(thislist, i):
    start = timeit.default_timer()
    test_list_append(thislist, i)
    end = timeit.default_timer()
    return end - start

'''
sys.stdout = open("append_output.txt", "w")
for i in range(1000000):
    print(i, timetest_append(thislist, i))
sys.stdout.close()'''


# our own experiment - testing runtime of append() by incrementing the number of appends done each time

thislist = []
def append_2(thislist, i):
    return thislist.append(i)

def timetest_append_2(thislist, i):
    start = timeit.default_timer()
    for _ in range(100*i):
        append_2(thislist, i)
    end = timeit.default_timer()
    return end - start

'''
sys.stdout = open("append_output2.txt", "w")
for i in range(1000):
    print(100*i, timetest_append_2(thislist, i))
sys.stdout.close()'''