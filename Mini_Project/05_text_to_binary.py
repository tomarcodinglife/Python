
text_input = input("Enter text to convert to binary: ")

def text_to_binary(text):
    binary_representation = ' '.join(format(ord(char), '08b') for char in text)
    return binary_representation

binary_output = text_to_binary(text_input)

print(f"'{text_input}' =  {binary_output}")
