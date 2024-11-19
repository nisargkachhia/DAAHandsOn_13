from collections import defaultdict

class GraphForTopoSort:
    def __init__(self):
        self.adjacency_list = defaultdict(list)
        self.all_nodes = set()

    def insert_edge(self, start, end):
        self.adjacency_list[start].append(end)
        self.all_nodes.update([start, end])

    def perform_topological_sort(self):
        indegrees = {node: 0 for node in self.all_nodes}
        for node in self.adjacency_list:
            for neighbor in self.adjacency_list[node]:
                indegrees[neighbor] += 1

        queue = [node for node in self.all_nodes if indegrees[node] == 0]
        sorted_nodes = []

        while queue:
            current = queue.pop(0)
            sorted_nodes.append(current)
            for neighbor in self.adjacency_list[current]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

        if any(indegrees.values()):
            raise Exception("The graph contains cycles; topological sort is not possible.")

        return sorted_nodes
