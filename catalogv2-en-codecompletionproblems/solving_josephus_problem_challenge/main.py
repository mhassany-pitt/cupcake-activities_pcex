# Define a Queue Class
class Queue:
        # Initializing the queue
        def __init__(self):
                self.items = []
        # Adding elements to the queue
        def enqueue(self,item):
                self.items.insert(0,item)
        # Removing elements from the queue
        def dequeue(self):
                return self.items.pop()
        # Checking the size of the queue
        def size(self):
                return  len(self.items)
# Define a function to solve Josephus problem
def circle(k,name_list):
        q = Queue()
        for i in range(len(name_list)):
        # We are trying to store the elements from the name_list into the queue structure
                q.enqueue(name_list[i])
        i = 0
        while q.size() != 1:
        # We are trying to count each element till the kth element
                temp = q.dequeue()
                if i != k:
                # We need to restore the non-kth elements so the Kth element is out of the queue.
                        q.enqueue(temp)
                else:
                        i = 0
                i += 1
        return q.dequeue()
name_list = ["Lily","David","Susan","Julia","David","Brad"]
print(circle(7,name_list))
