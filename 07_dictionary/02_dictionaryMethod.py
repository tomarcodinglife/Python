groceryRate = {
    "Salt" : "35",
    "Sugar" : "60",
    "mustardOil" : "180",
    "Cofee" : "300",
    "ghee" : "800"
}

# Key Method
print(groceryRate.keys()) # (['Salt', 'Sugar', 'mustardOil', 'Cofee', 'ghee'])

# Value Method
print(groceryRate.values()) # (['35', '60', '180', '300', '800'])

# Update Method
groceryRate.update({"ghee" : "750"})
print(groceryRate) # {'Salt': '35', 'Sugar': '60', 'mustardOil': '180', 'Cofee': '300', 'ghee': '750'}
groceryRate.update({"ghee" : "750", "DairyMilk" : "500"})
print(groceryRate) # {'Salt': '35', 'Sugar': '60', 'mustardOil': '180', 'Cofee': '300', 'ghee': '750', 'DairyMilk': '500'}

# get method
print(groceryRate.get("salt")) # None
print(groceryRate.get("Salt")) #  35

# different
print(groceryRate["Cofee"]) # 300
print(groceryRate.get("Cofee")) # 300

print(groceryRate.get("cofee")) # its provide in return - None (when you no key paires in dictionary)
# print(groceryRate["cofee"]) # its provide in return  - Error (when you no key paires in dictionary)

#  shallow copy of the dictionary
kitchenItem = groceryRate.copy()
print(kitchenItem) # {'Salt': '35', 'Sugar': '60', 'mustardOil': '180', 'Cofee': '300', 'ghee': '750', 'DairyMilk': '500'}

#  default value
print(kitchenItem.get("Cofee", None)) # 300
print(kitchenItem.get("tea", None)) # None

# pop 
car = {
    "Color" : "Black",
    "Price" : "5.6 lakh",
    "fuelType" : "Petrol"
}
print(car) # {'Color': 'Black', 'Price': '5.6 lakh', 'fuelType': 'Petrol'}
newCar = car.pop("Color")
print(car) # {'Price': '5.6 lakh', 'fuelType': 'Petrol'}

# pop items
employee = {
    "ID" : "565",
    "salary" : "3000000",
    "designation" : "AI Engineer"
}

print(employee) # {'ID': '565', 'salary': '3000000', 'designation': 'AI Engineer'}
newEmployee = employee.popitem()
print(newEmployee) # ('designation', 'AI Engineer')
print(employee) # {'ID': '565', 'salary': '3000000'}

# update
myDict = {"a" : "5", "b" : "10", "c" : "12"}
print(myDict) # {'a': '5', 'b': '10', 'c': '12'}
myDict.update({"d" : "12", "aman" : "252"})
print(myDict) # {'a': '5', 'b': '10', 'c': '12', 'd': '12', 'aman': '252'}

# fromkeys 
key = ['a', 'b', 'c']
newKeyVal = dict.fromkeys(key, 0) 
print(newKeyVal) # {'a': 0, 'b': 0, 'c': 0}

# is contain 
my_dict = {'a': 1, 'b': 2}
print('a' in my_dict)  # True
print('f' in my_dict)  # False

dict010 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(dict010) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
for key in dict010:
    print(key, dict010[key])
'''
a 1
b 2
c 3
d 4
e 5
'''

print(dict010.items()) 
# dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])

for key, value in dict010.items():
    print(key, value)
'''
a 1
b 2
c 3
d 4
e 5
'''
# question 
if "a" in dict010:
    print(dict010["a"])

# length of dictionary
print(len(dict010)) # 5


# dictionary update
dict005 = {'a': 1, 'b': 2}
dict006 = {'b': 3, 'c': 4}
dict005.update(dict006)
print(dict005) # {'a': 1, 'b': 3, 'c': 4}

#or

dict007 = {'a': 1, 'b': 2}
dict007["c"] = 3
print(dict007) # {'a': 1, 'b': 2, 'c': 3}

# dictionary delete
dictABC = {'a': 1, 'b': 2, 'c': 3}
del dictABC["a"]   # delete entry with key 'a'
print(dictABC) # {'b': 2, 'c': 3}


# dictionary clear
dict005.clear()
print(dict005) # {}

# dictionary under dictionary
dict008 = {
    "Name" : "Sujit",
    "Age" : 25,
    "Home" : {
        "City" : "Delhi",
        "State" : "Delhi",
        "Country" : "India"
    }
}

print(dict008) # {'Name': 'Sujit', 'Age': 25, 'Home': {'City': 'Delhi', 'State': 'Delhi', 'Country': 'India'}}
print(dict008["Home"]) # {'City': 'Delhi', 'State': 'Delhi', 'Country': 'India'}
print(dict008["Home"]["City"]) # Delhi

# dictionary inside list
dict009 = {
    "Name" : "Sujit",
    "Age" : 25,
    "Home" : ["Delhi", "Delhi", "India"]
}
print(dict009) # {'Name': 'Sujit', 'Age': 25, 'Home': ['Delhi', 'Delhi', 'India']}
print(dict009["Home"]) # ['Delhi', 'Delhi', 'India']

# squar number in dictionary
dict010 = {x: x**x for x in range(6)}
print(dict010) # {0: 1, 1: 1, 2: 4, 3: 27, 4: 256, 5: 3125}


# dictionary from keys and list
keys = ['a', 'b', 'c', 'd', 'e']
value = [1, 2, 3, 4, 5]
newDict = dict(zip(keys, value))
print(newDict) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# or 

keys01 = ['a', 'b', 'c', 'd', 'e']
value = 5
newDict01 = dict.fromkeys(keys01, value)
print(newDict01) # {'a': 5, 'b': 5, 'c': 5, 'd': 5, 'e': 5}