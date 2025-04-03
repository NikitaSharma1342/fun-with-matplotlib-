# Thinking, Fast and Slow Flowchart

This project visualizes the key concepts from Daniel Kahneman's book *Thinking, Fast and Slow* using a directed graph created with Python's `networkx` and `matplotlib` libraries. 

The flowchart provides a structured overview of the two systems of thinking, cognitive biases, decision-making principles, and strategies for improving decision-making.

## Features

- **Visualization of concepts**: Represents the hierarchy and relationships between key ideas from the book.
- **Layered arrangement**: Graph nodes are grouped by their logical flow (e.g., major ideas under Systems 1 and 2).
- **Custom styling**: Includes labeled nodes, directed edges, and spacing adjustments for clarity.

## Visualization

The output is a flowchart with the following layers:
1. **A** - The central concept: *Thinking, Fast and Slow*.
2. **B** - Two systems of thinking:
   - `System 1`: Fast, intuitive, automatic thinking.
   - `System 2`: Slow, analytical, effortful thinking.
3. **C** - Branches of related concepts:
   - Cognitive biases and heuristics.
   - Decision-making and prospect theory.
   - The two selves: experiencing vs. remembering.
4. **D** - Key takeaways for improving decision-making.

### Example Output

- A flowchart titled "Thinking, Fast and Slow Flowchart."
- Nodes are color-coded and labeled with concepts.
- Directed edges show relationships and flow between ideas.

## Installation

To get started, ensure you have Python 3.9 installed along with the following libraries:

- `networkx`
- `matplotlib`

You can install the required libraries via pip:

```bash
pip install networkx matplotlib
```

## Usage

1. Clone the repository or copy the script.
2. Run the script `flowchart.py` in any Python environment (PyCharm, Jupyter Notebook, etc.).
3. The script uses the following logic:
   - Nodes are defined with labels representing major ideas.
   - Relationships are represented with directed edges.
   - A layered layout (`multipartite_layout`) is used for positioning.
4. The flowchart is displayed using `matplotlib`.

### Run the Script

```bash
python flowchart.py
```

## File Structure

The project includes:
- **`flowchart.py`**: The main script that generates the visualization.

## Customization

- **Node Colors**: You can customize the colors by modifying the `node_color` in the code.
- **Graph Layout**: Adjust the layout or the scaling factors (`gap_x` and `gap_y`) to reposition the nodes.
- **Save as File**: To save the graph as an image, you can update the script to include:

  ```python
  plt.savefig('flowchart.png', dpi=300)
  ```

## Example Code Snippet

Here's a snippet showing how to define nodes and edges:

```python
# Define nodes with labels
nodes = {
    "A": "Thinking, Fast and Slow",
    "B1": "System 1 (Fast, Intuitive, Automatic)",
    "B2": "System 2 (Slow, Analytical, Effortful)",
}

# Add edges
edges = [
    ("A", "B1"),
    ("A", "B2"),
]
```

## Requirements

- Python 3.6 or higher
- Installed Python libraries: `networkx`, `matplotlib`

## Output Example

When you run the script, you will see a layered flowchart of the concepts from *Thinking, Fast and Slow*.

