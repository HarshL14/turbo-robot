import networkx as nx
# Create a directed graph
G = nx.DiGraph()
# Add edges
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A'), ('C', 'D'), ('D', 'A')])
# Compute PageRank
pagerank = nx.pagerank(G)
# Print the results
for node, value in pagerank.items():
    print(f"Node: {node}, PageRank: {value:.4f}")
