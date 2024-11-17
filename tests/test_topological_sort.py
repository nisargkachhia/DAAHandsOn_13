import unittest
from algorithms.topological_sort import Graph

class TestTopologicalSort(unittest.TestCase):
    def test_topological_sort(self):
        graph = Graph(6)
        graph.add_edge(5, 2)
        graph.add_edge(5, 0)
        graph.add_edge(4, 0)
        graph.add_edge(4, 1)
        graph.add_edge(2, 3)
        graph.add_edge(3, 1)

        result = graph.topological_sort()
        self.assertEqual(result, [5, 4, 2, 3, 1, 0])
