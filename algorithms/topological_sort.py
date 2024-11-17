from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort(self):
        visited = [False] * self.V
        stack = []

        def dfs(v):
            visited[v] = True
            for i in self.graph[v]:
                if not visited[i]:
                    dfs(i)
            stack.append(v)

        for i in range(self.V):
            if not visited[i]:
                dfs(i)

        return stack[::-1]
