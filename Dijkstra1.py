def max_bandwidth_no_heap(g, src, target):

    status = {}  # status map
    parent = {}  # store the parent of current vertex
    fringe = {} # fringes are stored in a list
    bw = {}  # bandwidth associated with each vertex

    for v in g.vertices():
        status[v] = 'unseen'

    bw[src] = float('inf')
    parent[src] = None
    status[src] = 'intree'

    for edge in g.incident_edges(src):
        v = get_opposite(edge, src)
        parent[v] = src
        status[v] = 'fringe'
        bw[v] = edge[2]
        fringe[v] = bw[v]

    while (len(fringe) != 0) and (not status[target] == 'intree'):
        weight, vertex = find_max(fringe)
        bw[vertex] = weight
        status[vertex] = 'intree'
        for edge in g.incident_edges(vertex):
            v = get_opposite(edge, vertex)
            w = edge[2]
            if status[v] == 'unseen':
                status[v] = 'fringe'
                parent[v] = vertex
                bw[v] = min(bw[vertex], w)
                fringe[v] = bw[v]
            elif status[v] == 'fringe' and bw[v] < min(bw[vertex], w):
                parent[v] = vertex
                bw[v] = min(bw[vertex], w)
                fringe[v] = bw[v]

    if not status[target] == 'intree':
        print('No such path from source to target!')
    maxbandwidth = bw[target]

    path =[]
    path.append(target)
    find_path(parent,src, target, path)
    path.reverse()
    return path, maxbandwidth

# trivial approach to find a fringe with max edge weight
def find_max(dict_data):
    """ find max in a list"""
    large = 0
    for key in dict_data:
        if dict_data[key] > large:
                large = dict_data[key]
                k = key
    del dict_data[k]
    return large, k

# recursion function to find the vertices on the maximum bandwidth path
def find_path(parent, s, t, path):
    if parent[t] != s:
        path.append(parent[t])
        find_path(parent, s, parent[t], path)
    else:
        path.append(s)

def get_opposite(edge, vertex):
    u, v, w = edge
    if u == vertex:
        return v
    else:
        return u
