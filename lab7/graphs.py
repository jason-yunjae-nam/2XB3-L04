from collections import deque
import random

#Undirected graph using an adjacency list - given in lab7.py file
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    # I commented this out because it's giving an error - I think whoever did this forgot to complete it?
    # def number_of_nodes():
    #     return len()

# shown in lecture
def create_random_graph(n, m):
    edge_list = []
    G = Graph(n)
    for i in range(n):
        for j in range(i):
            edge_list.append((i, j))
    for _ in range(m):
        edge = random.choice(edge_list)
        G.add_edge(edge[0], edge[1])
        edge_list.remove(edge)
    return G


#Breadth First Search - given in lab7.py file
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    print(Q)
    print(marked.items())
    for node in G.adj:
        if node != node1:
            marked[node] = False
    print(marked.items())
    while len(Q) != 0:
        current_node = Q.popleft()
        print(current_node)
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
            print(Q)
            print(marked.items())
    return False

#Depth First Search - given in lab7.py file
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    #print(marked.items())
    while len(S) != 0:
        #print(S)
        current_node = S.pop()
        #print(current_node)
        if not marked[current_node]:
            marked[current_node] = True
            #print(marked.items())
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False

# returns actual path instead of just true/false
def BFS2(G, node1, node2):
    Q = deque([node1])
    path = []
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        path.append(current_node)
        for node in G.adj[current_node]:
            if node == node2:
                path.append(node)
                return path
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return []

# returns actual path instead of just true/false
def DFS2(G, node1, node2):
    S = [node1]
    path = []
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        path.append(current_node)
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    path.append(node)
                    return path
                S.append(node)
    return []

a = Graph(6)
a.add_edge(0, 5)
a.add_edge(0, 1)
a.add_edge(0, 2)
a.add_edge(1, 2)
a.add_edge(1, 4)
a.add_edge(1, 0)
a.add_edge(1, 5)
a.add_edge(2, 1)
a.add_edge(2, 0)
a.add_edge(4, 1)
a.add_edge(5, 0)
a.add_edge(5, 1)
# print(a.adj)
# print(BFS2(a, 0, 4))

# a = {0: [5, 1, 2], 1: [2, 4, 0, 5], 2: [1, 0], 3: [], 4: [1], 5: [0, 1]}