# time testsimport timeit
import random 
import math
import sys

from rbt import *

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

class BSTNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def __str__(self):
        return "(" + str(self.value) + ")"

    def __repr__(self):
         return "(" + str(self.value) + ")"


class BST:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):
        if self.is_empty():
            self.root = BSTNode(value)
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = BSTNode(value)
                node.left.parent = node
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = BSTNode(value)
                node.right.parent = node
            else:
                self.__insert(node.right, value)
        
    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left == None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right == None:
            return "[" +  self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"




def test_height(a, b):
    L = create_random_list(10000)
    for i in L:
        a.insert(i)
        b.insert(i)

def test_height2(a, b, n):
    for i in range(1, n):
        a.insert(i)
        b.insert(i)

for i in range(1, 1000):
    a = RBTree()
    b = BST()
    test_height2(a, b, i)
    print(i, a.get_height(), b.get_height())


def test_factor(a, b, n):
    thislist = create_near_sorted_list(1000, n)
    for i in thislist:
        a.insert(i)
        b.insert(i)

for i in range(1, 100):
    a = RBTree()
    b = BST()
    test_factor(a, b, i/100)
    print(i, a.get_height(), b.get_height())
