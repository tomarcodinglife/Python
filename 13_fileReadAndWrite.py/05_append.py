# append
number_of_entry = int(input("Enter Number of Entry: "))
string = input("Input String: ")
file = open("C:/Users/PC/OneDrive/Documents/Python/13_fileReadAndWrite.py/appendFile.txt", "a")

totalString = ""

for i in range (number_of_entry):
    # string = input(f"Input String {i + 1} ")
    file.write(string + "\n")
    totalString += string

print(f"{number_of_entry} Entry of strings({totalString}) have been successfully appended to the file.")

file.close()
