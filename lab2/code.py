import timeit

def test_list_copy(n):
    thislist = list(range(1,n))
    newlist = thislist.copy()
    return newlist

def timetest_copy(runs, n):
    total = 0
    for _ in range(runs):
        start = timeit.default_timer()
        test_list_copy(n)
        end = timeit.default_timer()
        total += end - start
    return total/runs

'''
for i in range(1, 1000):
    print(i*100, timetest_copy(100, i*100))'''

#####

def test_list_lookup(thislist, i):
    return thislist[i]

def timetest_lookup(thislist, i):
    start = timeit.default_timer()
    test_list_lookup(thislist, i)
    end = timeit.default_timer()
    return end - start


thislist = list(range(1000000))
for i in range(len(thislist)):
    print(i, timetest_lookup(thislist, i))
