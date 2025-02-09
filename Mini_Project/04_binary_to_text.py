
binaryInput = input("Enter Binary Code: ")

def binary_to_Text(binaryString):
    binary_Value = binaryString.split()
    ascii_characters = [chr(int(bv, 2)) for bv in binary_Value]
    return ''.join(ascii_characters)

textOutput = binary_to_Text(binaryInput)
print(f"{binaryInput} = {textOutput}")