import math

class k_heap:
    length = 0
    data = []

    def __init__(self, values, k):
        self.k = k
        self.data = values
        self.length = len(values)
        self.build_heap()

    def build_heap(self):
        for i in range((self.length - 2) // self.k, -1, -1):
            #starts at last non leaf node (lowest parent) and will work upwards
            self.sink(i)

    def parent(self, i):
        # if node is root, return no parent
        if i == 0:
            return None
        return (i - 1) // self.k

    def children(self, i):
        kids = []
        for j in range(self.k):
            #if it is at the end of the heap (last leaf has already been set) return
            if (self.k*i) + (j + 1) > self.length - 1:
                return kids
            else:
                kids.append((self.k*i) + (j + 1))
        return kids

    def sink(self, i):
        #if node has no children, return as no swaps need to be made
        if self.children(i) == []:
            return

        largest_known = i
        #find largest child of i
        for j in self.children(i):
            if self.data[i] < self.data[j] and self.data[largest_known] < self.data[j]:
                largest_known = j

        #switch largest child with parent
        if largest_known != i:
            self.data[i], self.data[largest_known] = self.data[largest_known], self.data[i]
            #sink switched element if needed
            self.sink(largest_known)
<<<<<<< HEAD
=======

    def get_data(self):
        return self.data
>>>>>>> 1a61bdeccc0a0cc45cf2afbfe4850922f6f897a9
