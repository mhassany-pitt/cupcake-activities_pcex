# Step 1: Define Node class
class DoublyLinkedListNode:
        def __init__(self, initData):
                self.item = initData
                self.nref = None
                self.pref = None
# Step 2: Define the Doubly Linked List class
class DoublyLinkedList:
        def __init__(self):
                self.start_node = None
        def __str__(self):
                s = '['
                i = 0
                current = self.start_node
                while current != None:
                        if i != 0:
                                s = s + ', ' + current.item
                        else:
                                s = s + current.item
                        current = current.nref
                        i += 1
                return s + ']'
        def insert_at_start(self, data):
                new_node = DoublyLinkedListNode(data)
                if self.start_node is None:
                        self.start_node = new_node
                        return
                new_node.nref = self.start_node
                self.start_node.pref = new_node
                self.start_node = new_node
        def delete_at_end(self):
                if self.start_node is None:
                        print("The list has no element to delete")
                        return
                if self.start_node.nref is None:
                        self.start_node = None
                        return
                n = self.start_node
                while n.nref is not None:
                        n = n.nref
                n.pref.nref = None
# Step 3: Test the Linked List
dlist = DoublyLinkedList()
dlist.insert_at_start('Hugo')
dlist.insert_at_start('Mike')
dlist.insert_at_start('Riley')
dlist.insert_at_start('Greyson')
dlist.delete_at_end()
print(dlist)
