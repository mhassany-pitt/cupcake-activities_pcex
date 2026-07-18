# Define a Stack Class
class Stack:
        # Initializing the stack
        def __init__(self):
                self.items = []
        # Checking if the stack is empty
        def is_empty(self):
                return len(self.items) == 0
        # Adding elements to the stack
        def push(self, item):
                self.items.append(item)
        # Removing the elements from the stack
        def pop(self):
                return self.items.pop()
        # Checking the element in the stack
        def peek(self):
                if not self.is_empty():
                        return self.items[len(self.items) - 1]
        # Checking the size of the stack
        def size(self):
                return len(self.items)
s=Stack()
print(s.is_empty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.is_empty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())
