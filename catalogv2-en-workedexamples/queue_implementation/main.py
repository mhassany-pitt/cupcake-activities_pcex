# Define a Queue Class
class Queue:
        # Initializing the queue
        def __init__(self):
                self.items =[]
        # Adding elements to the queue
        def enqueue(self, item):
                self.items.insert(0,item)
        # Removing elements to the queue
        def dequeue(self):
                return self.items.pop()
        # Returning the queue as a string
        def __str__(self):
                return str(self.items)
q=Queue()
q.enqueue('cat')
q.enqueue(3)
print(q.dequeue())
print(q)
