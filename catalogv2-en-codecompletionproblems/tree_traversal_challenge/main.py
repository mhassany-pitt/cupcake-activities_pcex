# Define a binary tree class
class BinaryTree:
        def __init__(self, root):
                self.left = None
                self.right = None
                self.key = root
        # Define the Insert Node function
        def insert(self, data):
                if self.key:
                        if data < self.key:
                                if self.left is None:
                                        self.left = BinaryTree(data)
                                else:
                                        self.left.insert(data)
                        elif data > self.key:
                                if self.right is None:
                                        self.right = BinaryTree(data)
                                else:
                                        self.right.insert(data)
                else:
                        self.key = data
        # Define Post order traversal function
        def postorder_traversal(self, root):
                res = []
                if root:
                        res = self.postorder_traversal(root.left)
                        res = res + self.postorder_traversal(root.right)
                        res.append(root.key)
                return res
root = BinaryTree(5)
root.insert(14)
root.insert(16)
root.insert(3)
root.insert(4)
root.insert(10)
print(root.postorder_traversal(root))
