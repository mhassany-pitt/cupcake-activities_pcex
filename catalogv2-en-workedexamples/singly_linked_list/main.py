# Step 1: Define Node class
class SLinkedListNode:
        def __init__(self, initData, initNext):
                self.data = initData
                self.next = initNext
        def getData(self):
                return self.data
        def getNext(self):
                return self.next
        def setData(self, newData):
                self.data = newData
        def setNext(self, newNext):
                self.next = newNext
# Step 2: Define the Singly Linked List class
class SLinkedList:
        def __init__(self):
                self.head = None
                self.size = 0
        def __str__(self):
                s = '['
                i = 0
                current = self.head
                while current != None:
                        if i > 0:
                                s = s + ','
                        dataObject = current.getData()
                        if dataObject != None:
                                s = s + '%s' % dataObject
                                i = i + 1
                        current = current.getNext()
                s = s + ']'
                return s
        def append(self, item):
                temp = SLinkedListNode(item, None)
                if (self.head == None):
                        self.head = temp
                else:
                        current = self.head
                        while (current.getNext() != None):
                                current = current.getNext()
                        current.setNext(temp)
                self.size += 1
# Step 3: Test the Linked List
linked_list = SLinkedList()
linked_list.append('Hello')
linked_list.append('World')
print(linked_list)
