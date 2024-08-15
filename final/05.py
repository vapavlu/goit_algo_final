import uuid
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import to_hex
import numpy as np


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def get_color_gradient(num_colors):
    colors = plt.cm.Blues(np.linspace(0, 1, num_colors))
    return [to_hex(c) for c in colors]


def depth_first_search(root):
    stack = [root]
    colors = {}
    num_nodes = 0

    while stack:
        node = stack.pop()
        if node.id not in colors:
            colors[node.id] = num_nodes
            num_nodes += 1
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    
    return colors


def breadth_first_search(root):
    queue = [root]
    colors = {}
    num_nodes = 0

    while queue:
        node = queue.pop(0)
        if node.id not in colors:
            colors[node.id] = num_nodes
            num_nodes += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return colors


def draw_tree(tree_root, colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    color_gradient = get_color_gradient(len(colors))
    node_colors = {node_id: color_gradient[color_index] for node_id, color_index in colors.items()}
    
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=[node_colors.get(node, 'skyblue') for node in tree.nodes()])
    plt.show()


root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

dfs_colors = depth_first_search(root)
print("DFS Order:", dfs_colors)
draw_tree(root, dfs_colors)

bfs_colors = breadth_first_search(root)
print("BFS Order:", bfs_colors)
draw_tree(root, bfs_colors)