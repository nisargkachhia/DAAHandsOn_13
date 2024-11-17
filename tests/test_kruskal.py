import unittest
from algorithms.kruskal import Kruskal

class TestKruskal(unittest.TestCase):
    def test_kruskal_mst(self):
        kruskal = Kruskal(4)
        kruskal.add_edge(0, 1, 10)
        kruskal.add_edge(0, 2, 6)
        kruskal.add_edge(0, 3, 5)
        kruskal.add_edge(1, 3, 15)
        kruskal.add_edge(2, 3, 4)

        result = kruskal.kruskal_mst()
        expected = [(2, 3, 4), (0, 3, 5), (0, 1, 10)]
        self.assertEqual(result, expected)
