import random
import math


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

def mergesort_bottom(L):
    group = 1 #group divides the list into groups of 1, 2, 4, 8,...
    while group <= len(L):
        for i in range(0, len(L), 2*group):
            start = i
            mid = i + group - 1
            end = min(i + 2*group - 1, len(L)-1)
            merge_bottom(L, start, mid, end)
        group = 2*group
    return L

def merge_bottom(L, start, mid, end):
    a = L[start:mid+1]
    b = L[mid+1:end+1]
    combined = []
    while len(a)!=0 or len(b)!=0:
        # if a is empty, then copy rest of b to combined
        if len(a) == 0:
            combined += b
            b.clear()
        # if b is empty, then copy rest of a to combined
        elif len(b) == 0:
            combined += a
            a.clear()
        elif a[0] >= b[0]:
            combined.append(b[0])
            b.remove(b[0])
        elif a[0] < b[0]:
            combined.append(a[0])
            a.remove(a[0])
    counter = 0
    # copying sorted list combined to original list L
    for i in range(start, end+1):
        L[i] = combined[counter]
        counter+=1
    return L

# bottomup_test_list = create_random_list(100)
# print(bottomup_test_list)
# mergesort_bottom(bottomup_test_list)
# print(bottomup_test_list)


def mergesort_three(L):

    if len(L) <= 1:
        return 
    if len(L) == 2:
        if L[0] > L[1]:
            L[0], L[1] = L[1], L[0]
        return

    #Split the incoming list into three
    split = len(L)//3
    left, mid, right = L[:split], L[split : split+split], L[split+split:]

    #Mergesort_three core
    mergesort_three(left)
    mergesort_three(mid)
    mergesort_three(right)
    temp = merge_three(left, mid, right)

    for i in range(len(temp)):
        L[i] = temp[i]


def merge_three(left, mid, right):
    L = []
    i = j = k = 0

    while i < len(left) or j < len(mid) or k < len(right):
        if (i >= len(left)) and (j >= len(mid)):
            #if right is last list
            L.append(right[k])
            k += 1
        elif (i >= len(left)) and (k >= len(right)):
            #if mid is last list
            L.append(mid[j])
            j += 1
        elif (j >= len(mid)) and (k >= len(right)):
            #if left is last list
            L.append(left[i])
            i += 1
        elif i >= len(left):
            #if left finish first
            if mid[j] <= right[k]:
                L.append(mid[j])
                j += 1
            else:
                L.append(right[k])
                k+=1
        elif j >= len(mid):
            #if mid finish first
            if left[i] <= right[k]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[k])
                k +=1
        elif k >= len(right):
            #if right finish first
            if left[i] <= mid[j]:
                L.append(left[i])
                i += 1
            else:
                L.append(mid[j])
                j+=1
        else:
            #all still have values in lists
            #if left is smallest
            if (left[i] <= mid[j]) and (left[i] <= right[k]):
                L.append(left[i])
                i += 1
            #if mid is smallest
            elif (mid[j] <= left[i]) and (mid[j] <= right[k]):
                L.append(mid[j])
                j += 1
            #if right is smallest
            else:
                L.append(right[k])
                k += 1
    return L

# L = create_random_list(100)
# print("Random L: ", L)
# mergesort_three(L)
# print("Sorted L: ", L)

# tranditional mergesort provided in lab4.py file
def mergesort(L):
    
    if len(L) <= 1:
        return 
    mid = len(L)//2 
    left, right = L[:mid], L[mid:]

    #Mergesort core
    mergesort(left)
    mergesort(right)
    temp = merge(left, right)

    #Copy the sorted list to L
    for i in range(len(temp)):
        L[i] = temp[i]

def merge(left, right):
    L = []
    i = j = 0

    while i < len(left) or j < len(right):
        #Check it there's still elements to be merged from left and/or right
        if i >= len(left):
            L.append(right[j])
            j += 1
        elif j >= len(right):
            L.append(left[i])
            i += 1
        else:
            if left[i] <= right[j]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[j])
                j+=1
    return L

# quicksort implementation provided in lab3.py file - to compare mergesort
# and quicksort for near-sorted lists
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
