from collections import deque
import random
from graphs import *

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

def test_cycles(k, c, runs):
    #k = num of nodes
    #c = num of edges
    cycle = 0
    for i in range(runs):
        G = create_random_graph(k, c)
        if (has_cycle(G)):
            cycle += 1
    print(c, cycle/runs)

# for i in range(1, 101):
#     test_cycles(250, i*10, 20)

def test_connected(k, c, runs):
    connected = 0
    for i in range(runs):
        G = create_random_graph(k, c)
        if (is_connected(G)):
            connected += 1
    print(c, connected/runs)

for i in range(0, 100):
    test_connected(250, 200 + i*10, 50)


