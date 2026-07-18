# Define a binary tree class
class BinaryTree:
        def __init__(self, root):
                self.key = root
                self.left = None
                self.right = None
        # Define a function to insert node from the right
        def insert_right(self, new_node):
                if self.right is None:
                        self.right = BinaryTree(new_node)
                else:
                        node_tree = BinaryTree(new_node)
                        node_tree.right = self.right
                        self.right = node_tree
        # Define a function to print the tree
        def print_tree(self):
                if self.left:
                        self.left.print_tree()
                print(self.key, " ", end="")
                if self.right:
                        self.right.print_tree()
# Initializing a tree
root = BinaryTree(10)
root.insert_right(5)
root.insert_right(6)
root.insert_right(14)
root.print_tree()
