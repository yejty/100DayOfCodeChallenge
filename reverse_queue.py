from queue import Queue

q = Queue(maxsize=5)
q.put(1)
q.put(2)
print(q.get())  # Outputs 1 (FIFO)


#def reverse_queue():