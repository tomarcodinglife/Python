# When you multiple work in class and function component pack in single unit of code its called incapsulation
# When you hide implementation details hide from user and show only required details to user its called Abstraction
# incaplusation is a part of Abstraction it means when you hide implementation details from user its called incapsulation
# opps concept - 1. Inheritance 2. Polymorphism 3. Abstraction 4. Incapsulation

class employee:
    language = "Python"
    salary = 150000

# Yahaan ek class employee banayi hai, jisme do class-level variables hain:
# language: Yeh "Python" set kiya gaya hai, jo sabhi instances ke liye ek hi rahega.
# salary: Yeh 150000 set kiya gaya hai, jo sabhi instances ke liye ek hi salary dikhata hai.


    def __init__(self): # its call default constructor because its have no parameter
        self._name = " " #  # Initialize _name in the constructor
    
# __init__() ek constructor hai jo class ka instance banne par call hota hai.
# Yahaan aapne self._name ko ek khaali string " " se initialize kiya hai. self ka use current instance ko refer karne ke liye hota hai.

    @classmethod
    def showEmployee(self):
        print(f"employee of {self.language} & salary is {self.name}")

# @classmethod ka matlab hai ki yeh method class ke level par kaam karta hai, bina kisi specific instance ke. Yaani, aap ise bina kisi instance ke bhi call kar sakte hain.
# self.language aur self.name ke through class-level variable language aur instance property name ko access kiya ja raha hai.
# Yeh method employee ka language aur name dikhata hai.

    @property
    def name(self):
        return self.fullName 
    
#Yeh ek getter method hai jo instance ka fullName return karta hai.
# Is property ko employeeInstance.name ke roop mein directly access kiya ja sakta hai bina kisi parentheses ke.
    
    @name.setter 
    def name(self, string):
        self.fName = string.split(" ")[0]
        self.lName = string.split(" ")[1]
        self.fullName = self.fName + " " + self.lName
#Yeh setter method hai jo instance ka name set karta hai.
# Jab aap employeeInstance.name = "Sujit Tomar" likhenge, to yeh method run karega.
# Yeh input string ko space ke hisaab se split karega, aur pehla part fName (first name) aur doosra part lName (last name) mein store karega.
# Phir self.fullName mein yeh dono ko mila kar first name aur last name ko store karega.
    
employeeFirst = employee()
employeeFirst.name = "Sujit Tomar"
# employeeFirst.fatherName = "Sujit Kumar Singh"
print(employeeFirst.name)\

'''

'''