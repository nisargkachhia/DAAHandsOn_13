from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, start_vertex):
        visited = [False] * self.V
        result = []

        def dfs_util(v):
            visited[v] = True
            result.append(v)
            for neighbor in self.graph[v]:
                if not visited[neighbor]:
                    dfs_util(neighbor)

        dfs_util(start_vertex)
        return result
