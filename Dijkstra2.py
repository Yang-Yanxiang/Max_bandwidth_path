from adaptableHeapPriorityQueue import AdaptableHeapPriorityQueue

def max_bandwidth(g, src, target):
    status = {}  # status map
    parent = {}  # store the parent of current vertex
    fringe = AdaptableHeapPriorityQueue()  # fringes are stored at max heap data strucure
    bw = {}  # bandwidth associated with each vertex
    locator = {}  # locator to find specific one fringe in heap queue

    for v in g.vertices():
        status[v] = 'unseen'

    bw[src] = float('inf')
    parent[src] = None
    status[src] = 'intree'

    for edge in g.incident_edges(src):
        v = get_opposite(edge, src)
        w = edge[2]
        parent[v] = src
        status[v] = 'fringe'
        bw[v] = w
        locator[v] = fringe.add(bw[v], v)

    while len(fringe) != 1 and (not status[target] == 'intree'):
        weight,u = fringe.remove_max()
        del locator[u]
        bw[u] = weight
        status[u] = 'intree'
        for edge in g.incident_edges(u):
            v = get_opposite(edge, u)
            w = edge[2]
            if status[v] == 'unseen':
                status[v] = 'fringe'
                parent[v] = u
                bw[v] = min(bw[u], w)
                locator[v] = fringe.add(bw[v], v)
            elif status[v] == 'fringe' and bw[v] < min(bw[u], w):
                parent[v] = u
                bw[v] = min(bw[u], w)
                fringe.update(locator[v], bw[v], v)

    if not status[target] == 'intree':
        print('No such path from source to target!')

    maxbandwidth = bw[target]
    path =[]
    path.append(target)
    find_path(parent,src, target, path)
    path.reverse()
    return path, maxbandwidth

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