# tests/helper.py

import os

def load_graph_from_file(file_path):
    graph = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(' ')
            node = parts[0]
            neighbors = parts[1:]
            graph[node] = neighbors
    return graph
