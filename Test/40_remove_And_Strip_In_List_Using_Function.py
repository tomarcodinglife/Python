# remove in list by method
list = ["Sujit", "Amit", "Rohit", "Sumit", "Aman", "Ajit", "Rahul,", "Roushan"]

print(list) # ['Sujit', 'Amit', 'Rohit', 'Sumit', 'Aman', 'Ajit', 'Rahul,', 'Roushan']
list.remove("Sujit")
print(list) # ['Amit', 'Rohit', 'Sumit', 'Aman', 'Ajit', 'Rahul,', 'Roushan']


# append in list method
myList = []
myList.append("Delhi")
print(f"My List is : {myList}") # My List is : ['Delhi']

# strip method (it is check in last of word and remove from text)
word = "Sujit"
afWord = word.strip('it')
print(f"your word is {word} after strip your word is {afWord}")

# Remove in List Using Function

newList = ["Sujit", "Amit", "Rohit", "Sumit", "Aman", "Ajit", "Rahul,", "Roushan"]

def removeWordFromList(listName, word):
    for item in listName:
        listName.remove(word)
        return listName

print(removeWordFromList(newList, "Sumit"))# ['Sujit', 'Amit', 'Rohit', 'Aman', 'Ajit', 'Rahul,', 'Roushan']


def removeWordFromList(listName, word):
    functionList = []
    for item in listName:
        if not (item == word):
            functionList.append(item.strip(word))
        return functionList
    