import random

# lst = [43, 93, 98,69,76,32,97,31, 31,93, 123, 32,45]

def quicksort_inplace(L):
    inplace_helper(L, 0, len(L)-1)

def inplace_helper(L, right, left):
    if right >= left:
        return
    p_index = partition(L, right, left)
    inplace_helper(L, right, p_index-1)
    inplace_helper(L, p_index+1, left)

def partition(L, right, left):
    i = right
    j = right
    while j < left:
        if L[j] <= L[left]:
            L[i], L[j] = L[j], L[i]
            i += 1
        j += 1
    L[i], L[left] = L[left], L[i]
    return i

# quicksort_inplace(lst)
# print(lst)


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
    pivots = [L[0], L[len(L) - 1]]
    pivots.sort()
    pivot1 = pivots[0]
    pivot2 = pivots[1]
    left, mid, right = [], [], []
    
    for num in L[1:-1]:
        if num < pivot1: left.append(num)
        elif num > pivot2: right.append(num)
        else: mid.append(num)

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

    pivots = [L[0], L[1], L[len(L) - 1]]
    pivots.sort()
    pivot1 = pivots[0]
    pivot2 = pivots[1]
    pivot3 = pivots[2]
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

    pivots = [L[0], L[1], L[len(L) - 2], L[len(L) - 1]]
    pivots.sort()
    pivot1 = pivots[0]
    pivot2 = pivots[1]
    pivot3 = pivots[2] 
    pivot4 = pivots[3] 
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


# Elementary sorting algorithms
def bubble_sort(L):
    for i in range(len(L) - 1):
        for j in range(len(L) - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]

def selection_sort(L):
    for i in range(len(L)):
        min = i
        for j in range(i + 1, len(L)):
            if L[j] < L[min]:
                min = j
        L[i], L[min] = L[min], L[i]

def insertion_sort(L):
    for i in range(1, len(L)):
        item = L[i]
        j = i - 1
        while j >= 0 and L[j] > item:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = item

def insertion_sort_return(L):
    for i in range(1, len(L)):
        item = L[i]
        j = i - 1
        while j >= 0 and L[j] > item:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = item
    return L

def final_sort(L):
    copy = final_sort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]

def final_sort_copy(L):  
    if len(L) < 15:
        return insertion_sort_return(L)
    pivots = [L[0], L[len(L) - 1]]
    pivots.sort()
    pivot1 = pivots[0]
    pivot2 = pivots[1]
    left, mid, right = [], [], []
    
    for num in L[1:-1]:
        if num < pivot1: left.append(num)
        elif num > pivot2: right.append(num)
        else: mid.append(num)

    return final_sort_copy(left) + [pivot1] + final_sort_copy(mid) + [pivot2] + final_sort_copy(right)

# final_sort(lst)
# print(lst)