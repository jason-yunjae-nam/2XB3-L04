lst = [43, 93, 98,69,76,32,97,31, 31,93, 123, 32,45]

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

#print(quicksort_inplace(lst))


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

#my_quicksort(lst)
#print(lst)

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
    if (pivot1 > pivot2): pivot1, pivot2 = pivot2, pivot1  
    if (pivot2 > pivot3): pivot2, pivot3 = pivot3, pivot2  
    if (pivot1 > pivot2): pivot1, pivot2 = pivot2, pivot1
    left, lmid, rmid, right = [], [], [], []

    for num in L[2:-1]:
        if num < pivot1: left.append(num)
        elif pivot1 <= num < pivot2: lmid.append(num)
        elif pivot2 <= num < pivot3: rmid.append(num)
        else: right.append(num)

    return tri_quicksort_copy(left) + [pivot1] + tri_quicksort_copy(lmid) + [pivot2] + tri_quicksort_copy(rmid) + [pivot3] + tri_quicksort_copy(right)

#tri_pivot_quicksort(lst)
#print(lst)

def quad_pivot_quicksort(L):
    copy = quad_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quad_quicksort_copy(L):
    if len(L) < 4:
        if len(L) == 3:
            if L[0] > L[1]: L[0] , L[1] = L[1], L[0]
            if L[1] > L[2]: L[1] , L[2] = L[2], L[1]
            if L[0] > L[1]: L[0] , L[1] = L[1], L[0]
        if len(L) == 2 and L[0] > L[1]:
            L[0] , L[1] = L[1], L[0]
        return L

    pivot1 = L[0]
    pivot2 = L[len(L) - 1]
    pivot3 = L[1]
    pivot4 = L[len(L)-2]
    if (pivot1 > pivot2): pivot1, pivot2 = pivot2, pivot1  
    if (pivot2 > pivot3): pivot2, pivot3 = pivot3, pivot2  
    if (pivot3 > pivot4): pivot3, pivot4 = pivot4, pivot3
    if (pivot1 > pivot2): pivot1, pivot2 = pivot2, pivot1  
    if (pivot2 > pivot3): pivot2, pivot3 = pivot3, pivot2  
    if (pivot1 > pivot2): pivot1, pivot2 = pivot2, pivot1  
    left, lmid, mid, rmid, right = [], [], [], [], []

    for num in L[2:-2]:
        if num < pivot1: left.append(num)
        elif pivot1 <= num < pivot2: lmid.append(num)
        elif pivot2 <= num < pivot3: mid.append(num)
        elif pivot3 <= num < pivot4: rmid.append(num)
        else: right.append(num)

    return quad_quicksort_copy(left) + [pivot1] + quad_quicksort_copy(lmid) + [pivot2] + quad_quicksort_copy(mid) + [pivot3] + quad_quicksort_copy(rmid) + [pivot4] + quad_quicksort_copy(right)

#quad_pivot_quicksort(lst)
#print(lst)