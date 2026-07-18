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
                return self.items[- 1]
# Checking the if the brackets are matched
def match(bracket):
        left =['(','[','{']
        right={')',']','}'}
        s=Stack()
        for brackets in bracket:
                if brackets in left:
                        # We try to store the current bracket in the stack if it is the left one
                        s.push(brackets)
                elif brackets in right:
                        if s.is_empty():
                                return False
                        if 1 <= ord(brackets) - ord(s.peek()) <= 2:
                                # We try to empty the stack if any right bracket matches a left bracket in the stack.
                                s.pop()
        return s.is_empty()
expr1=['[','{','(','{','}',')','}',']']
expr2=['{','[','}','(',')']
print(match(expr1))
print(match(expr2))
