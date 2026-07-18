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
        # Define the search function that count how many times the target appears.
        def search(self, target):
                current = self.head
                count = 0
                while current is not None:
                        if current.data == target:
                                count += 1
                        current = current.next
                return count
linked_list = LinkedList()
linked_list.push(1)
linked_list.push(3)
linked_list.push(3)
linked_list.push(7)
linked_list.push(9)
linked_list.push(11)
linked_list.push(11)
target = 11
print("There are", linked_list.search(target), "instances of", target, "in the list")
