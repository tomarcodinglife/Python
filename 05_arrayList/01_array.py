fruits = ["Apple", "Orange", "Aakash", "Rohan", 5, 76.8]

print(fruits[2])

# ----------------------------------- Replace Method ------------------------------------
print("-------------------------------- Replace Method -------------------------------")

fruits[2] = "Grapes"
print(fruits[2])

# ----------------------------------- Sort Method ------------------------------------
print("-------------------------------- Sort Method -------------------------------")

number = [40, 52, 64, 25, 45, 78]
print(number) # [40, 52, 64, 25, 45, 78]
number.sort()
print(number) # [25, 40, 45, 52, 64, 78]

# ----------------------------------- Reverse Method ------------------------------------
print("-------------------------------- Reverse Method -------------------------------")

marks = [40, 52, 64, 25, 45, 78]
print(marks) # [40, 52, 64, 25, 45, 78]
marks.reverse() 
print(marks) # [78, 45, 25, 64, 52, 40]

# ----------------------------------- Insert Method ------------------------------------
print("-------------------------------- Insert Method -------------------------------")
array = [1, 2, 5, 6, 7, 8, 10]
print(array) # [1, 2, 5, 6, 7, 8, 10]
array.insert(2, 3) 
print(array) # [1, 2, 3, 5, 6, 7, 8, 10]
array.insert(3, 4)
print(array) # [1, 2, 3, 4, 5, 6, 7, 8, 10]
array.insert(8, 9)
print(array) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ----------------------------------- Pop Method ------------------------------------
print("-------------------------------- Pop Method -------------------------------")
arrayPop = [10, 20, 30, 40, 50]
print(arrayPop.pop(2)) # 30
print(arrayPop) # [10, 20, 40, 50]
valuePop = arrayPop.pop(3) 
print(valuePop) # 50

# ----------------------------------- Remove Method ------------------------------------
print("-------------------------------- Remove Method -------------------------------")
arrayRemove = ["Amit", "Sumit", "Ranjit", "Sanjit"]
print(arrayRemove.remove("Sanjit"))
print(arrayRemove) # ['Amit', 'Sumit', 'Ranjit']


# Sum
a = [1, 2, 3]
print(sum(a)) # 6


