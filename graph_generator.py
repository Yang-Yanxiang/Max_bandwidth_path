import graph
import random

# 5000 vertices
# 1. In the fire graph G1, every vertex has degree exacty 6
# 2. In the seconde graph G2, each vertex has edges going to about 20% of the other vertices;
# randomly assign positice weights to edges in the graphs

num_vertex = 5000
max_weight = 1000

def graph_generator1():
    """ 5000 vertices
    In this graph, every vertex has degree exacty 6
    """
    # Initialize a graph and insert 5000 vertices
    g = graph.Graph()
    for vertex_index in range(1, num_vertex+1):
        g.insert_vertex(vertex_index)

    source = random.randint(1, 2000)  # randomly select a source vertex
    target = random.randint(3000, 4999)  # ramdomly select a destination vertex

    # add a path from source vertex to target vertex
    curser = source
    for u in g.vertices():
        if u == target or u == source:
            continue
        else:
            weight = random.randint(1, max_weight)
            g.insert_edge(curser, u, weight)
            curser = u
    g.insert_edge(curser, target, random.randint(1, max_weight))

    # if the degree of any vertex is not 6, we generate a edge from this vertex
    #for u in range(1, num_vertex+1):
    #    while g.degree(u) < 6:
    #        v = random.randint(u, num_vertex)
    #        if g.degree(v) < 6:
    #            weight = random.randint(1,max_weight)
    #            g.insert_edge(u, v, weight)
    #        else:
    #            continue


    # if the degree of any vertex is less than 6, we generate a edge from this vertex
    candidates = set(i for i in range(1, num_vertex+1))
    while len(candidates) != 0:
        u = candidates.pop()
        while g.degree(u) < 6 and len(candidates) != 0:
            v = candidates.pop()
            if g.degree(v) < 6:
                weight = random.randint(1, max_weight)
                g.insert_edge(u, v, weight)
                if g.degree(v) < 6:
                    candidates.add(v)
            else:
                continue


    print('Nnmber of edges: ', g.edge_count())
    print('Number of vertices: ', g.vertex_count())

    # check if this graph satisfies our requirement. If not, print out error information
    # for vertex in g.vertices():
    #    if g.degree(vertex) != 6:
    #        print('Graph is not correct')

    print('graph generation end')
    return g, source, target

def graph_generator2():
    """
    5000 vertices
    In this graph, each vertex has edges going to about 20% of the other vertices;
    """
    print('*It will take a little bit time to generate graph 2, please wait patiently*')
    g = graph.Graph()
    for vertex_index in range(1, num_vertex+1):
        g.insert_vertex(vertex_index)

    source = random.randint(1, 50)  # randomly select a source vertex
    target = random.randint(4990, 4999)  # ramdomly select a destination vertex

    # add a path from source vertex to target vertex
    start = source
    for u in g.vertices():
        if u == target or u == source:
            continue
        else:
            weight = random.randint(1, max_weight)
            g.insert_edge(start, u, weight)
            start = u
    g.insert_edge(start, target, random.randint(1, max_weight))

    # if the degree of any vertex is less than 0.2 * number_of_vertex, we generate a edge from this vertex
    candidates = set(i for i in range(1, num_vertex+1))
    while len(candidates) != 0:
        u = candidates.pop()
        while g.degree(u) < 0.2*num_vertex:
            v = candidates.pop()
            if g.degree(v) < 0.2*num_vertex:
                weight = random.randint(1, max_weight)
                g.insert_edge(u, v, weight)
                if g.degree(v) < 0.2*num_vertex:
                    candidates.add(v)
            else:
                continue

    print('Nnmber of edges: ', g.edge_count())
    print('Number of vertices: ', g.vertex_count())

    # check the degree for each vertex. the probability of outgoing incident edges should be about 20%
    # for vertex in g.vertices():
    #    if g.degree(vertex) != 0.2*num_vertex:
    #        print('error')

    print('g generation end')
    return g, source, target

