def quicksort_inplace(L):
    if len(L) < 2:
        return L
    pivot = L[len(L)-1]
    left = -1
    right = 0
    for _ in range(len(L)-1):
        if L[right] > pivot:
            right+=1
        else:
            left+=1
            L[left], L[right] = L[right], L[left]
            right+=1
    L[left+1], L[len(L)-1] = L[len(L)-1], L[left+1]
    return quicksort_inplace(L[:left+1]) + [L[left+1]] + quicksort_inplace(L[left+2:])

#lst = [33,89,55,35,45,98,76,54,49]
lst = [43, 93, 98,69,76,32,97,31, 31,93]
#print(quicksort_inplace(lst))
    

"""
def my_quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)
"""


def dual_pivot_quicksort(L):
    copy = dual_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def dual_quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot1 = L[0]
    pivot2 = L[len(L) - 1]
    if (L[0] > L[len(L) - 1]):
        pivot1 = L[len(L) - 1]
        pivot2 = L[0]
    left, mid, right = [], [], []
    for num in L[1:-1]:
        if num < pivot1:
            left.append(num)
        elif num > pivot2:
            right.append(num)
        else:
            mid.append(num)
    return dual_quicksort_copy(left) + [pivot1] + dual_quicksort_copy(mid) + [pivot2] + dual_quicksort_copy(right)

#dual_pivot_quicksort(lst)
#print(lst)

def tri_pivot_quicksort(L):
    copy = tri_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def tri_quicksort_copy(L):
    if len(L) < 3:
        if len(L) == 2 and L[0] > L[1]:
            L[0] , L[1] = L[1], L[0]
        return L

    pivot1 = L[0]
    pivot2 = L[len(L) - 1]
    pivot3 = L[1]
    if (pivot1 > pivot2):
        pivot1, pivot2 = pivot2, pivot1  
    if (pivot2 > pivot3):
        pivot2, pivot3 = pivot3, pivot2  
    if (pivot1 > pivot2):
        pivot1, pivot2 = pivot2, pivot1
    left, lmid, rmid, right = [], [], [], []

    for num in L[2:-1]:
        if num <= pivot1:
            left.append(num)
        elif num >= pivot3:
            right.append(num)
        elif (num > pivot1) and (num < pivot2):
            lmid.append(num)
        else:
            rmid.append(num)
    return tri_quicksort_copy(left) + [pivot1] + tri_quicksort_copy(lmid) + [pivot2] + tri_quicksort_copy(rmid) + [pivot3] + tri_quicksort_copy(right)

tri_pivot_quicksort(lst)
print(lst)