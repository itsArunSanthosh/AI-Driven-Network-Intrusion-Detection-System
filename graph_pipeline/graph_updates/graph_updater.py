class GraphUpdater:
    def __init__(self, graph_builder):
        self.graph_builder = graph_builder

    def update(self, flow: dict):
        src = flow["src_ip"]
        dst = flow["dst_ip"]

        self.graph_builder.add_edge(src, dst)

        return self.graph_builder.get_graph()