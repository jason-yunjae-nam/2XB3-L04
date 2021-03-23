import math

#Undirected graph using an adjacency list
class WeightedGraph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        for edge in self.adj[node1]:
            if edge[0] == node2:
                return True
        return False

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2, weight):
        if node1 not in self.adj[node2]:
            self.adj[node1].append((node2, weight))
            self.adj[node2].append((node1, weight))

    def w(self, node1, node2):
        for edge_info in self.adj[node1]:
            if node2 == edge_info[0]:
                return edge_info[1]

    def number_of_nodes(self):
        return len(self.adj)

class MinHeap:
    length = 0
    data = []

    def __init__(self, L):
        self.data = L
        self.length = len(L)
        self.map = {}
        for i in range(len(L)):
            self.map[L[i].value] = i
        self.build_heap()

    def build_heap(self):
        for i in range(self.length // 2 - 1, -1, -1):
            self.sink(i)

    def sink(self, i):
        smallest_known = i
        if self.left(i) < self.length and self.data[self.left(i)].key < self.data[i].key:
            smallest_known = self.left(i)
        if self.right(i) < self.length and self.data[self.right(i)].key < self.data[smallest_known].key:
            smallest_known = self.right(i)
        if smallest_known != i:
            self.data[i], self.data[smallest_known] = self.data[smallest_known], self.data[i]
            self.map[self.data[i].value] = i
            self.map[self.data[smallest_known].value] = smallest_known
            self.sink(smallest_known)

    def insert(self, element):
        if len(self.data) == self.length:
            self.data.append(element)
        else:
            self.data[self.length] = element
        self.map[element.value] = self.length
        self.length += 1
        self.swim(self.length - 1)

    def insert_elements(self, L):
        for element in L:
            self.insert(element)

    def swim(self, i):
        while i > 0 and self.data[i].key < self.data[self.parent(i)].key:
            self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
            self.map[self.data[i].value] = i
            self.map[self.data[self.parent(i)].value] = self.parent(i)
            i = self.parent(i)

    def get_min(self):
        if len(self.data) > 0:
            return self.data[0]
  
    def extract_min(self):
        self.data[0], self.data[self.length - 1] = self.data[self.length - 1], self.data[0]
        self.map[self.data[self.length - 1].value] = self.length - 1
        self.map[self.data[0].value] = 0
        min_element = self.data[self.length - 1]
        self.length -= 1
        self.map.pop(min_element.value)
        self.sink(0)
        return min_element

    def decrease_key(self, value, new_key):
        if new_key >= self.data[self.map[value]].key:
            return
        index = self.map[value]
        self.data[index].key = new_key
        self.swim(index)

    def get_element_from_value(self, value):
        return self.data[self.map[value]]

    def is_empty(self):
        return self.length == 0
    
    def left(self, i):
        return 2 * (i + 1) - 1

    def right(self, i):
        return 2 * (i + 1)

    def parent(self, i):
        return (i + 1) // 2 - 1

    def __str__(self):
        height = math.ceil(math.log(self.length + 1, 2))
        whitespace = 2 ** height
        s = ""
        for i in range(height):
            for j in range(2 ** i - 1, min(2 ** (i + 1) - 1, self.length)):
                s += " " * whitespace
                s += str(self.data[j]) + " "
            s += "\n"
            whitespace = whitespace // 2
        return s

class Element:

    def __init__(self, value, key):
        self.value = value
        self.key = key

    def __str__(self):
        return "(" + str(self.value) + "," + str(self.key) + ")" 

def prim1(G):
    temp = G
    nodes = list(temp.adj)
    min_span_tree = WeightedGraph(G.number_of_nodes())
    A = [nodes[0]]
    for i in range(temp.number_of_nodes()):
        temp.adj[i].sort(key = lambda x: x[1])
    print(temp.adj)
    for j in range(G.number_of_nodes()-1):
        print(A)
        min_edge_weight = 1001
        min_node = A[0]
        print("j:", j)
        if j == G.number_of_nodes() - 2:
            for i in nodes:
                if i not in A:
                    final_node = i
            min_span_tree.add_edge(final_node, temp.adj[final_node][0][0], temp.adj[final_node][0][1])
            return min_span_tree
        for i in A:
            print("i:", i)
            if len(temp.adj[i]) != 0:
                print("here: ", temp.adj[i][0][1], temp.adj[i][0][0])
            if len(temp.adj[i]) != 0 and temp.adj[i][0][1] < min_edge_weight and temp.adj[i][0][0] not in A:
                min_edge_weight = temp.adj[i][0][1]
                min_node = i
                print("hmm")
            print("yup: ", min_edge_weight, min_node)
            
        if min_edge_weight != 1001:
            min_span_tree.add_edge(min_node, temp.adj[min_node][0][0], min_edge_weight)
            other_node = temp.adj[min_node][0][0]
            print("hi: ", other_node)
            print(min_span_tree.adj)
            print(temp.adj[min_node])
            print(temp.adj[other_node])
            temp.adj[min_node].pop(0)
            temp.adj[other_node].remove((min_node, min_edge_weight))
            A.append(other_node)
        else:
            print("I am here")   #never made it to here
            for i in A:
                temp.adj[i].pop(0)
        print(temp.adj)
    return min_span_tree

#first attempt (just changed everything to do with temp and used heaps, not very efficient)
# def prim2(G):
#     temp = G
#     nodes = list(temp.adj)
#     min_span_tree = WeightedGraph(G.number_of_nodes())
#     A = [nodes[0]]
#     for i in range(temp.number_of_nodes()):
#         temp.adj[i].sort(key = lambda x: x[1])
#     print(temp.adj)
#     #make heaps for each node adj, where the min will be the lowest weight relation
#     heaps = []
#     for k in nodes:
#         nodes2 = []
#         for m in temp.adj[k]:
#             print(temp.adj[k], m)
#             a = Element(m[0], m[1])
#             print(m[0], m[1])
#             nodes2.append(a)
#         heaps.append(nodes2)
#     #heaps2 is list of heaps at each node, heaps is list of lists to make heaps
#     heaps2 = []
#     for i in heaps:
#         b = MinHeap(i)
#         heaps2.append(b)
#     # print("hmm: ", heaps2[0].get_min().key)

#     #heaps2 is now gonna replace the temp.adj implementation below
#     #go through G and find best path while removing from heaps in heap2
#     for j in range(G.number_of_nodes()-1):
#         min_edge_weight = 1001
#         min_node = A[0]
#         if j == G.number_of_nodes() - 2:
#             for i in nodes:
#                 if i not in A:
#                     final_node = i
#             min_span_tree.add_edge(final_node, heaps2[final_node].get_min().value, heaps2[final_node].get_min().key)
#             return min_span_tree
#         for i in A:
#             if not heaps2[i].is_empty() and heaps2[i].get_min().key < min_edge_weight and heaps2[i].get_min().value not in A:
#                 min_edge_weight = heaps2[i].get_min().key 
#                 print("ew: ", min_edge_weight)
#                 min_node = i
#         print("mew: ", min_edge_weight , i)
#         if min_edge_weight != 1001:
#             min_span_tree.add_edge(min_node, heaps2[min_node].get_min().value, min_edge_weight)
#             other_node = heaps2[min_node].get_min().value
#             heaps2[min_node].extract_min()
#             # temp.adj[other_node].remove((min_node, min_edge_weight))
#             A.append(other_node)
#         else:
#             for i in A:
#                 heaps2[i].extract_min()
#     return min_span_tree

#second attempt lol didn't finish it cuz I don't get the infinite heap thing
#gotta use decrease key somehow but idk
# def prim2(G):
#     temp = G
#     nodes = list(temp.adj)
#     min_span_tree = WeightedGraph(G.number_of_nodes())
#     A = nodes[0]
#     #make a heap for each node in each loop
#     #the min will be the least weighted node to be used in A
#     for i in range(len(temp.adj)):
#         #elements is list of elements at node i
#         elements = []
#         for j in range(len(temp.adj[i])):
#             #adds all elements in adj to heap for that node, just adds value, key = 1001
#             elements.append(Element(temp.adj[i][0], 1001))
#         #heap is heap of elements at that node, min is lowest weight rn 1001 until decrease
#         heap = MinHeap(elements)

a = WeightedGraph(10)
a.add_edge(0, 8, 3)
a.add_edge(0, 1, 6)
a.add_edge(0, 7, 9)
a.add_edge(1, 8, 4)
a.add_edge(1, 6, 9)
a.add_edge(1, 5, 2)
a.add_edge(2, 7, 8)
a.add_edge(2, 5, 8)
a.add_edge(2, 8, 9)
a.add_edge(2, 6, 7)
a.add_edge(2, 4, 9)
a.add_edge(3, 7, 18)
a.add_edge(3, 4, 3)
a.add_edge(3, 9, 4)
a.add_edge(4, 9, 1)
a.add_edge(4, 6, 5)
a.add_edge(5, 8, 2)
a.add_edge(5, 6, 9)
a.add_edge(6, 9, 4)
a.add_edge(7, 8, 9)

# b = WeightedGraph(7)
# b.add_edge(0, 5, 4)
# b.add_edge(0, 3, 9)
# b.add_edge(0, 1, 7)
# b.add_edge(0, 4, 2)
# b.add_edge(1, 4, 13)
# b.add_edge(1, 2, 6)
# b.add_edge(1, 6, 3)
# b.add_edge(1, 3, 8)
# b.add_edge(1, 5, 11)
# b.add_edge(2, 4, 1)
# b.add_edge(2, 6, 5)
# b.add_edge(3, 5, 12)
# b.add_edge(3, 6, 14)
# b.add_edge(4, 6, 10)

#print(b.adj)
tester = prim2(a)
print("\n")
print(tester.adj)
