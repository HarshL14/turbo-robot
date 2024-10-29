def page_rank(graph, num_iterations=100, d=0.85):
    # Initialize the PageRank values
    num_nodes = len(graph)
    ranks = {node: 1 / num_nodes for node in graph}

    # Perform the PageRank algorithm
    for _ in range(num_iterations):
        new_ranks = {}
        for node in graph:
            rank_sum = sum(ranks[neighbor] / len(graph[neighbor]) for neighbor in graph if node in graph[neighbor])
            new_ranks[node] = (1 - d) / num_nodes + d * rank_sum
        ranks = new_ranks

    return ranks

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': ['A'],
    'D': ['C']
}

# Calculate PageRank
page_ranks = page_rank(graph)

# Print the PageRank of each node
for node, rank in page_ranks.items():
    print(f"Node {node} has PageRank: {rank:.4f}")
