#write a function to reverse a string
def reverse_string(input_string):
    output_string = ""
    for i in range(len(input_string), 0, -1):
        output_string += input_string[i-1]
    return output_string

print(reverse_string("abeceda"))