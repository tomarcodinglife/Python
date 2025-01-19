dictionary = {}

name = input("Enter Name: ")
language = input("Enter Language: ") # Sujit
dictionary.update({name: language}) # CPP
print(dictionary) # {'Sujit': 'CPP'}

name = input("Enter Name: ")  # Amit
language = input("Enter Language: ") # Python
dictionary.update({name: language}) 
print(dictionary) # {'Sujit': 'CPP', 'Amit': 'Python'}

name = input("Enter Name: ") # Rahul
language = input("Enter Language: ") # Java
dictionary.update({name: language}) 
print(dictionary) # {'Sujit': 'CPP', 'Amit': 'Python', 'Rahul': 'Java'}

name = input("Enter Name: ") # Rohan
language = input("Enter Language: ") # Javascript
dictionary.update({name: language})
print(dictionary) # {'Sujit': 'CPP', 'Amit': 'Python', 'Rahul': 'Java', 'Rohan': 'Javascript'}