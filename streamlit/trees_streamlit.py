import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from collections import deque
import time

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node.left is None:
                node.left = Node(value)
                return
            elif node.right is None:
                node.right = Node(value)
                return
            else:
                queue.append(node.left)
                queue.append(node.right)

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        
        self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

def create_tree_graph(root, is_bst=False):
    G = nx.DiGraph()
    
    if root is None:
        return G
    
    def add_edges(node, node_id):
        if node.left:
            left_id = id(node.left)
            G.add_node(left_id, value=node.left.value)
            G.add_edge(node_id, left_id)
            add_edges(node.left, left_id)
        
        if node.right:
            right_id = id(node.right)
            G.add_node(right_id, value=node.right.value)
            G.add_edge(node_id, right_id)
            add_edges(node.right, right_id)
    
    root_id = id(root)
    G.add_node(root_id, value=root.value)
    add_edges(root, root_id)
    
    return G

def visualize_tree(root, is_bst=False, highlight_path=None):
    if root is None:
        st.write("Tree is empty")
        return
    
    G = create_tree_graph(root, is_bst)
    
    pos = hierarchy_pos(G, id(root))
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    node_colors = ['skyblue' for _ in G.nodes()]
    
    if highlight_path:
        path_nodes = [id(node) for node in highlight_path]
        for i, node_id in enumerate(G.nodes()):
            if node_id in path_nodes:
                node_colors[i] = 'lightgreen'
    
    nx.draw(G, pos, with_labels=False, node_color=node_colors, 
            node_size=700, arrows=False, ax=ax)
    
    # Draw node labels
    node_labels = {node_id: G.nodes[node_id]['value'] for node_id in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=12)
    
    plt.title("Binary Search Tree" if is_bst else "Binary Tree")
    st.pyplot(fig)

def hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=0, xcenter=0.5):
    """
    Position nodes in a hierarchical layout.
    Based on implementation by Joel Cornett.
    """
    def _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter, pos=None, parent=None, parsed=[]):
        if pos is None:
            pos = {root: (xcenter, vert_loc)}
        else:
            pos[root] = (xcenter, vert_loc)
        children = list(G.neighbors(root))
        if parent is not None:
            children.remove(parent)
        if len(children) != 0:
            dx = width / len(children)
            nextx = xcenter - width/2 - dx/2
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G, child, dx, vert_gap, vert_loc-vert_gap, nextx, pos, root, parsed)
        return pos
    
    return _hierarchy_pos(G, root, width, vert_gap, vert_loc, xcenter)

def traverse_tree(root, mode="in-order"):
    result = []
    
    def in_order(node):
        if node:
            in_order(node.left)
            result.append(node.value)
            in_order(node.right)
    
    def pre_order(node):
        if node:
            result.append(node.value)
            pre_order(node.left)
            pre_order(node.right)
    
    def post_order(node):
        if node:
            post_order(node.left)
            post_order(node.right)
            result.append(node.value)
    
    def level_order(node):
        if not node:
            return
        
        queue = deque([node])
        while queue:
            current = queue.popleft()
            result.append(current.value)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    
    if mode == "in-order":
        in_order(root)
    elif mode == "pre-order":
        pre_order(root)
    elif mode == "post-order":
        post_order(root)
    elif mode == "level-order":
        level_order(root)
    
    return result

def traverse_tree_with_steps(root, mode="in-order"):
    if root is None:
        return []
    
    if mode == "in-order":
        return in_order_with_steps(root)
    elif mode == "pre-order":
        return pre_order_with_steps(root)
    elif mode == "post-order":
        return post_order_with_steps(root)
    elif mode == "level-order":
        return level_order_with_steps(root)

def in_order_with_steps(root):
    steps = []
    
    def traverse(node, path=None):
        if path is None:
            path = []
        
        if node:
            path.append(node)
            traverse(node.left, path.copy())
            steps.append((node, path.copy(), "Visit"))
            traverse(node.right, path.copy())
    
    traverse(root)
    return steps

def pre_order_with_steps(root):
    steps = []
    
    def traverse(node, path=None):
        if path is None:
            path = []
        
        if node:
            path.append(node)
            steps.append((node, path.copy(), "Visit"))
            traverse(node.left, path.copy())
            traverse(node.right, path.copy())
    
    traverse(root)
    return steps

def post_order_with_steps(root):
    steps = []
    
    def traverse(node, path=None):
        if path is None:
            path = []
        
        if node:
            path.append(node)
            traverse(node.left, path.copy())
            traverse(node.right, path.copy())
            steps.append((node, path.copy(), "Visit"))
    
    traverse(root)
    return steps

def level_order_with_steps(root):
    steps = []
    
    if not root:
        return steps
    
    queue = deque([(root, [root])])
    while queue:
        node, path = queue.popleft()
        steps.append((node, path, "Visit"))
        
        if node.left:
            new_path = path.copy()
            new_path.append(node.left)
            queue.append((node.left, new_path))
        
        if node.right:
            new_path = path.copy()
            new_path.append(node.right)
            queue.append((node.right, new_path))
    
    return steps

def search_with_steps(root, value):
    steps = []
    
    def search(node, path=None):
        if path is None:
            path = []
        
        if node is None:
            return None, steps
        
        path.append(node)
        steps.append((node, path.copy(), "Checking"))
        
        if node.value == value:
            steps.append((node, path.copy(), "Found"))
            return node, steps
        
        if value < node.value:
            steps.append((node, path.copy(), "Going Left"))
            return search(node.left, path.copy())
        
        steps.append((node, path.copy(), "Going Right"))
        return search(node.right, path.copy())
    
    result, steps = search(root)
    return steps

def main():
    st.title("Interactive Tree Visualization")
    
    st.sidebar.header("Control Panel")
    tree_type = st.sidebar.radio("Select Tree Type", ["Binary Tree", "Binary Search Tree"])
    
    # Initialize session state variables if they don't exist
    if 'bt' not in st.session_state:
        st.session_state.bt = BinaryTree()
    
    if 'bst' not in st.session_state:
        st.session_state.bst = BinarySearchTree()
    
    if 'current_tree' not in st.session_state:
        st.session_state.current_tree = 'bt' if tree_type == "Binary Tree" else 'bst'
    else:
        st.session_state.current_tree = 'bt' if tree_type == "Binary Tree" else 'bst'
    
    if 'highlight_path' not in st.session_state:
        st.session_state.highlight_path = None
    
    # Get current tree based on selection
    current_tree = st.session_state.bt if st.session_state.current_tree == 'bt' else st.session_state.bst
    
    # Input for adding nodes
    with st.sidebar.form("add_node_form"):
        new_value = st.number_input("Enter value to add:", min_value=0, max_value=100, step=1)
        submit_button = st.form_submit_button("Add Node")
    
    if submit_button:
        if tree_type == "Binary Tree":
            st.session_state.bt.insert(new_value)
        else:
            st.session_state.bst.insert(new_value)
        st.session_state.highlight_path = None
    
    # BST-specific operations
    if tree_type == "Binary Search Tree":
        st.sidebar.subheader("BST Operations")
        search_value = st.sidebar.number_input("Enter value to search:", min_value=0, max_value=100, step=1)
        if st.sidebar.button("Search"):
            steps = search_with_steps(st.session_state.bst.root, search_value)
            if steps:
                # Animate the search steps
                progress_bar = st.sidebar.progress(0)
                status_text = st.sidebar.empty()
                
                for i, (node, path, action) in enumerate(steps):
                    st.session_state.highlight_path = path
                    progress = int((i+1) / len(steps) * 100)
                    progress_bar.progress(progress)
                    status_text.text(f"Step {i+1}/{len(steps)}: {action} node {node.value}")
                    
                    # Re-render the tree (this forces a redraw)
                    st.experimental_rerun()
                    time.sleep(1)  # Pause between steps
    
    # Tree traversal
    st.sidebar.subheader("Tree Traversal")
    traversal_mode = st.sidebar.selectbox(
        "Select Traversal Method", 
        ["in-order", "pre-order", "post-order", "level-order"]
    )
    
    if st.sidebar.button("Traverse"):
        if current_tree.root:
            steps = traverse_tree_with_steps(current_tree.root, traversal_mode)
            
            # Display the traversal result
            traversal_result = traverse_tree(current_tree.root, traversal_mode)
            st.sidebar.write(f"Traversal Result: {traversal_result}")
            
            # Animate the traversal steps
            progress_bar = st.sidebar.progress(0)
            status_text = st.sidebar.empty()
            
            for i, (node, path, action) in enumerate(steps):
                st.session_state.highlight_path = path
                progress = int((i+1) / len(steps) * 100)
                progress_bar.progress(progress)
                status_text.text(f"Step {i+1}/{len(steps)}: {action} node {node.value}")
                
                # Re-render the tree (this forces a redraw)
                st.experimental_rerun()
                time.sleep(1)  # Pause between steps
    
    # Add preset trees
    st.sidebar.subheader("Preset Trees")
    if st.sidebar.button("Create Sample Binary Tree"):
        st.session_state.bt = BinaryTree()
        for value in [10, 5, 15, 3, 7, 12, 18]:
            st.session_state.bt.insert(value)
        st.session_state.highlight_path = None
    
    if st.sidebar.button("Create Sample BST"):
        st.session_state.bst = BinarySearchTree()
        for value in [10, 5, 15, 3, 7, 12, 18]:
            st.session_state.bst.insert(value)
        st.session_state.highlight_path = None
    
    # Clear tree
    if st.sidebar.button("Clear Current Tree"):
        if tree_type == "Binary Tree":
            st.session_state.bt = BinaryTree()
        else:
            st.session_state.bst = BinarySearchTree()
        st.session_state.highlight_path = None
    
    # Explanation section
    with st.expander("How it works"):
        if tree_type == "Binary Tree":
            st.markdown("""
            ## Binary Tree
            
            A binary tree is a tree data structure in which each node has at most two children, referred to as the left child and the right child.
            
            ### Properties:
            - Each node has at most two children
            - Nodes are added level by level from left to right
            - This is also called a "level-order" insertion
            
            ### Time Complexity:
            - Search: O(n) in worst case
            - Insertion: O(1) if we know the position, O(n) to find position
            - Deletion: O(n) to find and remove node
            
            ### Common Applications:
            - Expression trees in compilers
            - Huffman coding trees for data compression
            - File system organization
            """)
        else:
            st.markdown("""
            ## Binary Search Tree (BST)
            
            A binary search tree is a binary tree with the following properties:
            - The left subtree of a node contains only nodes with keys lesser than the node's key
            - The right subtree of a node contains only nodes with keys greater than the node's key
            - The left and right subtree each must also be a binary search tree
            
            ### Properties:
            - Enables efficient searching, insertion, and deletion
            - Maintains sorted order
            - Left child < Parent < Right child
            
            ### Time Complexity:
            - Search: O(log n) average, O(n) worst case
            - Insertion: O(log n) average, O(n) worst case
            - Deletion: O(log n) average, O(n) worst case
            
            ### Common Applications:
            - Dictionary implementations
            - Database indexing
            - Priority queues
            - Expression evaluation
            """)
    
    # Tree visualization
    st.header("Tree Visualization")
    if tree_type == "Binary Tree":
        visualize_tree(st.session_state.bt.root, False, st.session_state.highlight_path)
    else:
        visualize_tree(st.session_state.bst.root, True, st.session_state.highlight_path)
    
    # Code playground
    with st.expander("Code Playground"):
        code = st.text_area("Write your own tree operations:", 
            """# Example: Count the number of nodes in the tree
def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# Get current tree
current_tree = st.session_state.bt.root if st.session_state.current_tree == 'bt' else st.session_state.bst.root

# Run the function and print result
result = count_nodes(current_tree)
print(f"Number of nodes: {result}")
""", height=300)
        
        if st.button("Run Code"):
            try:
                # Get current tree for code execution
                locals_dict = {
                    'st': st,
                    'BinaryTree': BinaryTree,
                    'BinarySearchTree': BinarySearchTree,
                    'Node': Node
                }
                
                # Execute code
                exec(code, globals(), locals_dict)
            except Exception as e:
                st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()