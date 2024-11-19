from collections import defaultdict

def dfs_traversal(edges, start_node):
    graph = defaultdict(list)
    for source, destination in edges:
        graph[source].append(destination)

    visited_nodes = set()

    def recursive_dfs(node):
        if node not in visited_nodes:
            print(node, end=" ")
            visited_nodes.add(node)
            for adjacent in graph[node]:
                recursive_dfs(adjacent)

    recursive_dfs(start_node)
    print()  
