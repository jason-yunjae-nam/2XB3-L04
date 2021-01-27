import timeit

def test_list_copy(n):
    thislist = list(range(1,n))
    newlist = thislist.copy()
    return newlist

def timetest(runs, n):
    total = 0
    for _ in range(runs):
        start = timeit.default_timer()
        test_list_copy(n)
        end = timeit.default_timer()
        total += end - start
    return total/runs

for i in range(1, 1000):
    print(i*100, timetest(100, i*100))