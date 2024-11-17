import unittest
from algorithms.dfs import Graph

class TestDFS(unittest.TestCase):
    def test_dfs(self):
        graph = Graph(4)
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        graph.add_edge(1, 2)
        graph.add_edge(2, 0)
        graph.add_edge(2, 3)
        graph.add_edge(3, 3)

        result = graph.dfs(2)
        self.assertEqual(result, [2, 0, 1, 3])
