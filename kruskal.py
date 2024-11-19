class GraphForKruskal:
    def __init__(self):
        self.edges = []

    def add_edge(self, node1, node2, weight):
        self.edges.append((node1, node2, weight))

    def find_set(self, parent, node):
        if parent[node] == node:
            return node
        return self.find_set(parent, parent[node])

    def union_sets(self, parent, rank, root1, root2):
        if rank[root1] < rank[root2]:
            parent[root1] = root2
        elif rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root2] = root1
            rank[root1] += 1

    def compute_mst(self):
        mst = []
        self.edges.sort(key=lambda edge: edge[2])
        parent, rank = {}, {}

        for edge in self.edges:
            u, v, _ = edge
            if u not in parent:
                parent[u] = u
                rank[u] = 0
            if v not in parent:
                parent[v] = v
                rank[v] = 0

        edge_count = 0
        index = 0

        while edge_count < len(parent) - 1:
            u, v, weight = self.edges[index]
            index += 1
            root1 = self.find_set(parent, u)
            root2 = self.find_set(parent, v)

            if root1 != root2:
                edge_count += 1
                mst.append((u, v, weight))
                self.union_sets(parent, rank, root1, root2)

        return mst
