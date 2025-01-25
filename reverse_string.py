#can use a stack?
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def print_stack(self):
        print("Stack contents:", self.stack)

def reverse_string_stack(input_string):
    num_of_char = len(input_string)
    output_string = ""
    stack = Stack()

    # Push each character onto the stack
    for i in range(num_of_char): #O(n)
        #print(input_string[i])
        stack.push(input_string[i])

    #stack.print_stack()

    # Pop each character from the stack to reverse the string
    for i in range(num_of_char): #O(n)
        #print(stack.peek())
        output_string += stack.pop() #O(n)

    #stack.print_stack()
    return output_string

#write a function to reverse a string
def reverse_string(input_string):
    output_string = ""
    for i in range(len(input_string), 0, -1): #O(n)
        output_string += input_string[i-1]  #O(n)
    return output_string

print(reverse_string("abeceda"))
print(reverse_string_stack("abeceda"))

import io
def reverse_string(input_string):
    # Create a StringIO object to store the reversed string
    string_builder = io.StringIO()
    
    # Iterate through the input string in reverse order
    for char in reversed(input_string): # O(n)
        string_builder.write(char) # O(1)
    
    # Retrieve the reversed string
    reversed_string = string_builder.getvalue()
    
    return reversed_string

# Example usage
original = "Hello, World!"
reversed_result = reverse_string(original)
print(f"Original: {original}")
print(f"Reversed: {reversed_result}")
