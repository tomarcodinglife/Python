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
# newKeyVal = key.fromkeys(key, 0)
# print(newKeyVal)

# is contain 
my_dict = {'a': 1, 'b': 2}
# print('a' in my_dict) 
# print('f' in my_dict) 