from IPython import get_ipython
from IPython.display import display
# %%

import networkx as nx
from pyvis.network import Network

# Create a new directed graph
G = nx.DiGraph()

# Define concepts with color and shape
concepts = {
    "Machine Learning": {"color": "gold", "shape": "ellipse"},
    "Supervised Learning": {"color": "lightblue", "shape": "box"},
    "Unsupervised Learning": {"color": "lightgreen", "shape": "box"},
    "Linear Regression": {"color": "blue", "shape": "dot"},
    "Logistic Regression": {"color": "blue", "shape": "dot"},
    "Decision Trees": {"color": "blue", "shape": "dot"},
    "k-NN": {"color": "blue", "shape": "dot"},
    "SVM": {"color": "blue", "shape": "dot"},
    "Naive Bayes": {"color": "blue", "shape": "dot"},
    "K-Means Clustering": {"color": "green", "shape": "dot"},
    "PCA": {"color": "green", "shape": "dot"},
    "Neural Networks": {"color": "orange", "shape": "dot"},
    "Gradient Descent": {"color": "red", "shape": "star"},
    "Loss Function": {"color": "red", "shape": "star"}
}

# Add nodes
for concept, attr in concepts.items():
    G.add_node(concept, title=concept, color=attr["color"], shape=attr["shape"])

# Define relationships (edges)
edges = [
    ("Machine Learning", "Supervised Learning"),
    ("Machine Learning", "Unsupervised Learning"),
    ("Supervised Learning", "Linear Regression"),
    ("Supervised Learning", "Logistic Regression"),
    ("Supervised Learning", "Decision Trees"),
    ("Supervised Learning", "k-NN"),
    ("Supervised Learning", "SVM"),
    ("Supervised Learning", "Naive Bayes"),
    ("Unsupervised Learning", "K-Means Clustering"),
    ("Unsupervised Learning", "PCA"),
    ("Machine Learning", "Neural Networks"),
    ("Linear Regression", "Gradient Descent"),
    ("Logistic Regression", "Gradient Descent"),
    ("Neural Networks", "Gradient Descent"),
    ("Neural Networks", "Loss Function"),
    ("Linear Regression", "Loss Function"),
    ("Logistic Regression", "Loss Function")
]

# Add edges
G.add_edges_from(edges)

# Create PyVis interactive network
net = Network(height="700px", width="100%", bgcolor="#222222", font_color="white")
net.from_nx(G)
# Explicitly set notebook=False to avoid potential rendering issues in some environments
net.show("ml_concept_map.html")