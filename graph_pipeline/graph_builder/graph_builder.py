from collections import defaultdict

class GraphBuilder:
    def __init__(self):
        self.graph = defaultdict(set)

    def add_edge(self, src: str, dst: str):
        self.graph[src].add(dst)

    def get_graph(self):
        return self.graph