class Kruskal:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal_mst(self):
        self.edges.sort(key=lambda x: x[2])
        parent = list(range(self.V))
        rank = [0] * self.V
        mst = []

        for u, v, weight in self.edges:
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)
            if root_u != root_v:
                mst.append((u, v, weight))
                self.union(parent, rank, root_u, root_v)

        return mst
