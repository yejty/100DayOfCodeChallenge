class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def enqueue(self, item):
        self.items.append(item)

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else: 
            return None
        
    def dequeue(self):
        if not self.is_empty():
            front_item = self.items[0]
            self.items.remove(front_item)
            return front_item
        else: 
            raise IndexError("Dequeue from an empty queue") 
        
    def clear(self):
        self.items.clear()

    def print_queue(self):
        print(self.items)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
'''print(queue.size())
print(queue.peek())
print(queue.dequeue())
print(queue.is_empty())
queue.clear()
print(queue.is_empty())
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.print_queue()'''

def reverse_queue(queue):
    print("Queue")
    queue.print_queue()
    items = []

    for i in range(queue.size()):
        items.append(queue.dequeue())

    for i in range(len(items), 0, -1):
        queue.enqueue(items[i-1])
        
    print("Reversed queue")
    queue.print_queue()
    
reverse_queue(queue)