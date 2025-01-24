class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def peek(self):
        if not self.is_empty():
            return self.items[self.size()-1]
        else: 
            return None
        
    def pop(self):
        if not self.is_empty():
            last_item = self.items[self.size()-1]
            self.items.remove(last_item)
            return last_item
        else: 
            raise IndexError("Pop from an empty stack") 
        
    def clear(self):
        self.items.clear()

    def print_stack(self):
        print(self.items)

stack = Stack()
stack.push(1)
stack.print_stack()
stack.push(2)
stack.print_stack()
stack.push(3)
stack.print_stack()
stack.peek()
stack.print_stack()
stack.pop()
stack.print_stack()
stack.push(8)
stack.size()
stack.print_stack()
stack.clear()
stack.print_stack()