class Graph:
    def __init__(self, directed = False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return set(self._outgoing.keys())

    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing.keys())
        if self.is_directed() == True:
            return total
        else:
            return total//2

    def edges(self):
        edge_set = set()
        for map in self._outgoing.values():
             edge_set.update(map.values())
        return edge_set

    def neighbors(self, v):
        return self._outgoing[v].keys()

    def get_edge(self, u, v):
        return self._outgoing[u].get(v)

    def degree(self, v,outgoing = True ):
        return len(self._outgoing[v]) if outgoing == True else len(self._incoming[v])

    def incident_edges(self, v):
        return self._outgoing[v].values()

    def is_directed(self):
        return self._outgoing is not self._incoming

    def insert_vertex(self, vertex_index):
        self._outgoing[vertex_index] = {}
        if self.is_directed() == True:
            self._incoming[vertex_index] = {}

    def insert_edge(self, u, v, weight):
        self._outgoing[u][v] = (u, v, weight)
        self._incoming[v][u] = (u, v, weight)

