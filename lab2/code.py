import timeit
import sys

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


#for i in range(1, 1000):
#    print(i*100, timetest_copy(100, i*100))

#####

def test_list_lookup(thislist, i):
    return thislist[i]

def timetest_lookup(thislist, i):
    start = timeit.default_timer()
    test_list_lookup(thislist, i)
    end = timeit.default_timer()
    return end - start


# thislist = list(range(1000000))
# sys.stdout = open("lookup_output.txt", "w")
# for i in range(len(thislist)):
#     print(i, timetest_lookup(thislist, i))
# sys.stdout.close()

thislist = []
def test_list_append(thislist, i):
    return thislist.append(i)

def timetest_append(thislist, i):
    start = timeit.default_timer()
    test_list_append(thislist, i)
    end = timeit.default_timer()
    return end - start

sys.stdout = open("append_output.txt", "w")
for i in range(1000000):
    print(timetest_append(thislist, i))
sys.stdout.close()
