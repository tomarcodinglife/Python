Word = "Ram"

with open ("C:/Users/PC/OneDrive/Documents/Python/Test/48_writeFile.txt", "r") as file:
    sentance = file.read()

wordnew  = sentance.replace(Word, "####")

with open ("C:/Users/PC/OneDrive/Documents/Python/Test/48_writeFile.txt", "w") as file:
   file.write(Word)