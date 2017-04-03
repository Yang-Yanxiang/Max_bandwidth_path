from heapPriorityQueue import HeapPriorityQueue
import graph
from queue import *

parent = {}
rank = {}

def make_set(vertex):
    parent[vertex] = vertex
    rank[vertex] = 0

def find(vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent[vertex])
    return parent[vertex]

def union(vertex1, vertex2):
    root1 = find(vertex1)
    root2 = find(vertex2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            rank[root1] += 1

def maximum_st_kruskal(g, src, target):

    maximum_spanning_tree = graph.Graph()                  # list of edges in spanning tree
    pq = HeapPriorityQueue()
    
    for v in g.vertices():
        make_set(v)

    for e in g.edges():
        pq.add(e[2], e)

    while not pq.is_empty():
        weight, edge = pq.remove_max()
        u, v, w = edge
        root_of_u = find(u)
        root_of_v = find(v)
        if root_of_u != root_of_v:
            if u not in maximum_spanning_tree.vertices():
                maximum_spanning_tree.insert_vertex(u)
            if v not in maximum_spanning_tree.vertices():
                maximum_spanning_tree.insert_vertex(v)
            maximum_spanning_tree.insert_edge(*edge)
            union(u, v)

    path = bfs_find_path(maximum_spanning_tree,src,target)
    edge_on_path = []
    for i in range(len(path)-1):
        edge_on_path.append(g.get_edge(path[i], path[i+1])[2])
    max_bandwidth = min(edge_on_path)
    return path, max_bandwidth

def bfs_find_path(graph, start, end):
    q = Queue()
    temp_path = [start]
    q.put(temp_path)
    while not q.empty():
        temp_path = q.get()
        last_node = temp_path[len(temp_path) -1]
        if last_node == end:
            return temp_path
        for link_node in graph.neighbors(last_node):
            if link_node not in temp_path:
                new_path = temp_path + [link_node]
                q.put(new_path)