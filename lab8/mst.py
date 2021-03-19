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
                print(temp.adj[i][0][1], temp.adj[i][0][0])
            if len(temp.adj[i]) != 0 and temp.adj[i][0][1] < min_edge_weight and temp.adj[i][0][0] not in A:
                min_edge_weight = temp.adj[i][0][1]
                min_node = i
            print(min_edge_weight, min_node)
            
        if min_edge_weight != 1001:
            min_span_tree.add_edge(min_node, temp.adj[min_node][0][0], min_edge_weight)
            other_node = temp.adj[min_node][0][0]
            print(other_node)
            print(min_span_tree.adj)
            print(temp.adj[min_node])
            print(temp.adj[other_node])
            temp.adj[min_node].pop(0)
            temp.adj[other_node].remove((min_node, min_edge_weight))
            A.append(other_node)
        else:
            print("I am here")
            for i in A:
                temp.adj[i].pop(0)
        print(temp.adj)
    return min_span_tree

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

b = WeightedGraph(7)
b.add_edge(0, 5, 4)
b.add_edge(0, 3, 9)
b.add_edge(0, 1, 7)
b.add_edge(0, 4, 2)
b.add_edge(1, 4, 13)
b.add_edge(1, 2, 6)
b.add_edge(1, 6, 3)
b.add_edge(1, 3, 8)
b.add_edge(1, 5, 11)
b.add_edge(2, 4, 1)
b.add_edge(2, 6, 5)
b.add_edge(3, 5, 12)
b.add_edge(3, 6, 14)
b.add_edge(4, 6, 10)


#print(b.adj)
tester = prim1(a)
print("\n")
print(tester.adj)
