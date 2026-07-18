# Define a Node class
class Node:
        def __init__(self, data):
                self.data = data
                self.next = None
# Define a LinkedList class
class LinkedList:
        def __init__(self):
                self.head = None
        def push(self, new):
                new_node = Node(new)
                new_node.next = self.head
                self.head = new_node
        # Define the search function
        def search(self, target):
                current = self.head
                while current is not None:
                        if current.data == target:
                                return True
                        current = current.next
                return False
linked_list = LinkedList()
linked_list.push(1)
linked_list.push(3)
linked_list.push(3)
linked_list.push(7)
linked_list.push(9)
linked_list.push(11)
linked_list.push(11)
target = 11
# Calling the search function
if (linked_list.search(target)):
        print("Found", target, "in list")
else:
        print("Did not find", target, "in list")
