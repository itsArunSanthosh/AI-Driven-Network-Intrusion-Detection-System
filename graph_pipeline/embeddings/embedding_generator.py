"""
Generates simple node embeddings from graph structure.

Note: Placeholder for advanced GNN-based embeddings.
"""

def generate_embedding(graph: dict, node: str) -> dict:
    neighbors = graph.get(node, set())

    return {
        "node": node,
        "degree": len(neighbors),
        "normalized_degree": len(neighbors) / (len(graph) + 1e-5)
    }