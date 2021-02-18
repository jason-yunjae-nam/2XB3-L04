# starttotal = timeit.default_timer()
# #stuff and things
# endtotal = timeit.default_timer()
# totaltotal = 0
# totaltotal += endtotal - starttotal
# print("total time = ", totaltotal)


# #test copy()
import timeit
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
    #worst case is that right is the largest list with (split + 2) entries
    #other case besides perfect three is (split + 1) entires

    #Mergesort_three core
    mergesort_three(left)
    mergesort_three(mid)
    mergesort_three(right)
    temp = merge_three(left, mid, right)
    print("temp: ", temp)

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
            #if right is last list
            L.append(left[i])
            i += 1
        elif i >= len(left):
            print("here")
            #if left finish first
            if mid[j] <= right[k]:
                L.append(mid[j])
                j += 1
            else:
                L.append(right[k])
                k+=1
        elif j >= len(mid):
            print("here2")
            #if mid finish first
            if left[i] <= right[k]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[k])
                k +=1
        elif k >= len(right):
            print("here3")
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

L = create_random_list(100)
print("Random L: ", L)
mergesort_three(L)
print("Sorted L: ", L)


def mergesort(L):
    
    if len(L) <= 1:
        return 
    mid = len(L)//2 
    left, right = L[:mid], L[mid:]

    print(left, right)
    #Mergesort core
    mergesort(left)
    mergesort(right)
    temp = merge(left, right)
    print("temp: ", temp)

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
