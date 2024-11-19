from topological_sort import GraphForTopoSort
from dfs import dfs_traversal
from kruskal import GraphForKruskal

# Topological Sort Example
topo_graph = GraphForTopoSort()
topo_graph.insert_edge('undershorts', 'socks')
topo_graph.insert_edge('undershorts', 'pants')
topo_graph.insert_edge('pants', 'belt')
topo_graph.insert_edge('socks', 'belt')
topo_graph.insert_edge('shirt', 'tie')
topo_graph.insert_edge('tie', 'undershorts')
topo_graph.insert_edge('belt', 'jacket')
topo_graph.insert_edge('jacket', 'shoes')

print("Topological Sort Result:")
print(topo_graph.perform_topological_sort())

# DFS Example
edges = [
    ("a", "b"),
    ("a", "c"),
    ("b", "d"),
    ("c", "e"),
    ("e", "f"),
    ("f", "g"),
    ("g", "h"),
]
print("\nDFS Traversal:")
dfs_traversal(edges, 'a')

# Kruskal's Algorithm Example
kruskal_graph = GraphForKruskal()
kruskal_graph.add_edge('A', 'B', 1)
kruskal_graph.add_edge('B', 'C', 4)
kruskal_graph.add_edge('A', 'C', 3)
kruskal_graph.add_edge('C', 'D', 2)

print("\nMinimum Spanning Tree Using Kruskal's Algorithm:")
print(kruskal_graph.compute_mst())
