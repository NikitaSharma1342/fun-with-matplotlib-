import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
flowchart = nx.DiGraph()

# Add nodes with labels
nodes = {
    "A": "Thinking, Fast and Slow",
    "B1": "System 1 (Fast, Intuitive, Automatic)",
    "B2": "System 2 (Slow, Analytical, Effortful)",
    "C1": "Cognitive Biases & Heuristics",
    "C2": "Decision-Making & Prospect Theory",
    "C3": "The Two Selves: Experiencing vs. Remembering",
    "D": "Key Takeaway: Improving Decision-Making",
    "C1a": "Anchoring Bias",
    "C1b": "Availability Heuristic",
    "C1c": "Confirmation Bias",
    "C1d": "Loss Aversion",
    "C1e": "Overconfidence Bias",
    "C2a": "People don’t evaluate risks rationally",
    "C2b": "We weigh potential losses more than gains",
    "C2c": "Choices depend on framing",
    "C3a": "Experiencing Self: Lives in the moment",
    "C3b": "Remembering Self: Creates a story based on peaks & endings",
    "D1": "Be aware of cognitive biases",
    "D2": "Engage System 2 for critical decisions",
    "D3": "Understand how framing & emotions influence choices",
    "D4": "Recognize when intuition is helpful vs. misleading"
}

# Add all nodes to the graph
for node, label in nodes.items():
    # Add subset attribute based on the first character of the node ID
    layer = node[0]  # grouping nodes A, B, C, D based on first letter
    flowchart.add_node(node, label=label, subset=layer)

# Add edges for the flowchart
edges = [
    ("A", "B1"), ("A", "B2"), ("B1", "C1"), ("B2", "C2"),
    ("B1", "C3"), ("B2", "C3"), ("C1", "C1a"), ("C1", "C1b"),
    ("C1", "C1c"), ("C1", "C1d"), ("C1", "C1e"), ("C2", "C2a"),
    ("C2", "C2b"), ("C2", "C2c"), ("C3", "C3a"), ("C3", "C3b"),
    ("C1", "D"), ("C2", "D"), ("C3", "D"), ("D", "D1"),
    ("D", "D2"), ("D", "D3"), ("D", "D4")
]
flowchart.add_edges_from(edges)

# Define node positions for visualization (layered as in the original flowchart)
pos = nx.multipartite_layout(flowchart, subset_key="subset")

# Introduce gaps manually by scaling the layout positions
gap_x = 5  # Horizontal gap scaling factor
gap_y = 5  # Vertical gap scaling factor

for node in pos:
    pos[node] = (pos[node][0] * gap_x, pos[node][1] * gap_y)

# Draw the graph
plt.figure(figsize=(18, 18))
node_labels = nx.get_node_attributes(flowchart, 'label')
nx.draw_networkx_edges(flowchart, pos, arrows=True, alpha=0.5)
nx.draw_networkx_labels(flowchart, pos, labels=node_labels, font_size=8)
nx.draw_networkx_nodes(flowchart, pos, node_color="lightblue", node_size=2000, edgecolors="lightblue")

# Add title and display the flowchart
plt.title("Thinking, Fast and Slow Flowchart")
plt.axis("off")
plt.show()
