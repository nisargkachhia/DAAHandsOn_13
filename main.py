from algorithms.topological_sort import Graph as TopoGraph
from algorithms.dfs import Graph as DFSGraph
from algorithms.kruskal import Kruskal

# Example: Topological Sort
topo_graph = TopoGraph(6)
topo_graph.add_edge(5, 2)
topo_graph.add_edge(5, 0)
topo_graph.add_edge(4, 0)
topo_graph.add_edge(4, 1)
topo_graph.add_edge(2, 3)
topo_graph.add_edge(3, 1)
print("Topological Sort:", topo_graph.topological_sort())

# Example: Depth-First Search
dfs_graph = DFSGraph(4)
dfs_graph.add_edge(0, 1)
dfs_graph.add_edge(0, 2)
dfs_graph.add_edge(1, 2)
dfs_graph.add_edge(2, 0)
dfs_graph.add_edge(2, 3)
dfs_graph.add_edge(3, 3)
print("DFS:", dfs_graph.dfs(2))

# Example: Kruskal's Algorithm
kruskal = Kruskal(4)
kruskal.add_edge(0, 1, 10)
kruskal.add_edge(0, 2, 6)
kruskal.add_edge(0, 3, 5)
kruskal.add_edge(1, 3, 15)
kruskal.add_edge(2, 3, 4)
print("Kruskal's MST:", kruskal.kruskal_mst())
