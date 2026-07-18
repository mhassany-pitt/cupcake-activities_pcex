# Define a binary tree class
class BinaryTree:
        def __init__(self, root):
                self.key = root
                self.left = None
                self.right = None
        # Define a function to insert node from the left
        def insert_left(self, new_node):
                if self.left is None:
                        self.left = BinaryTree(new_node)
                else:
                        node_tree = BinaryTree(new_node)
                        node_tree.left = self.left
                        self.left = node_tree
        # Define a function to print the tree
        def print_tree(self):
                if self.left:
                        self.left.print_tree()
                print(self.key, " ", end="")
                if self.right:
                        self.right.print_tree()
# Initializing a tree
root = BinaryTree(10)
root.insert_left(5)
root.insert_left(6)
root.insert_left(14)
root.print_tree()
