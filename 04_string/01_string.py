# String Writing in Python

# -------------- String Introduction -----------------------
print("-------------- String Introduction -----------------------")

name1 = 'Sujit Tomar'
name2 = "Sujit Tomar"
name3 = '''Sujit Tomar'''

nameIdx = name1[4] 
names = name2[0:5] # it means last index (5) is not included when you print
name = name2[-5] # T


print(nameIdx) # t
print(names) # Sujit
print(name) # T

print(name2[:3]) # is same as print name[0:3] - Suj
print(name1[1:]) # is same as print name[1:9] - ujit Tomar
print(name[:]) # sujit

# -------------- Negative Slicing -----------------------
print("-------------- Negative Slicing -----------------------")

string = "Sujit" # in this string total index = 4, but string length = 5

print(string[:3]) # it means [0:3] - Suj
print(string[3:]) # it means [3:length of string] means [3:5] - it
print(string[3:4]) # i


# --------------------- String Function --------------------------
print("--------------------- String Function --------------------------")

studentName = "sujit tomar"

print(len(studentName)) # 11
print(studentName.endswith("mar")) # True
print(studentName.endswith("abc")) # false
print(studentName.startswith("Suj")) # True
print(studentName.startswith("abc")) # false
print(studentName.capitalize()) # Sujit tomar
print(studentName.upper()) # SUJIT TOAMR
print(studentName.count("t")) # 2 times t in this string

print(studentName.find("tomar")) # 6

newStudendName = studentName.replace("tomar", "kumar singh") 
print(newStudendName) # sujit kumar singh
print(newStudendName.title()) # Sujit Kumar Singh
print(newStudendName.split()) # ['sujit', 'kumar', 'singh']

# Remove White Space
programmingLanguage = "     Python          "
print(programmingLanguage.strip()) # Python 


# Joint 
anyName = ["Sujit", "Tomar"]
print("".join(anyName)) #SujitTomar
print(" ".join(anyName)) #Sujit Tomar


# String is alpha ?  Returns True if all characters in the string are alphabetic (no numbers or symbols).
abcName = "Sujit 1421 Kumar"
abcdName = "Sujit"
print(abcName.isalpha()) # False
print(abcdName.isalpha()) # True
print(abcName.isnumeric()) # False
print(abcdName.isnumeric()) # False
print(abcdName.isalpha()) # True


certificateNumber = "525522"
print(certificateNumber.isdigit()) # True
print(certificateNumber.isnumeric()) # True

marks = "75.62"
print(marks.isdigit()) # False
print(marks.isnumeric()) # False

# Width
roll = "139"
print(roll.zfill(5)) # 00139

# Separator
myText = "Sujit, Tomar"
print(myText.partition(", ")) # ('Sujit', ', ', 'Tomar')

# string formating
collegeName = "Hello, {}!"
print(collegeName.format("World")) # Hello, World!
print(collegeName.format("Python")) # Hello, Python!


# String Encoding
teacherName = "Dr. A. K Prakash"
encoded = teacherName.encode("utf-8")
print(encoded) # b'Dr. A. K Prakash

# String Swap Case
myString = "Hello World"
print(myString.swapcase()) # hELLO wORLD

