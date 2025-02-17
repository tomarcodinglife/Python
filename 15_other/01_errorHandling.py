# Method First

name = " "

try:
    print(name)
except AttributeError as e:
    print("Error", e)



# Method Second
fullName = "Sujit Tomar"
# def abc() pass

try:
    print(fullName)
except AttributeError as e:
        print("Error", e)

file = open("15_other/test.txt", 'w')

try:
     file.write("Sujit Tomar")
finally:
     file.close()



try:
     pass
except:
     pass
finally:
     pass
