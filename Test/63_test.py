class wish:
    def __init__(self, message):
        self.message = message
        

    def wish01(self):
        print(self.message)
    
    @staticmethod
    def wish02():
        print("Thank You")
    
Message01 = wish("Your Welcome Sir/Madam")
Message01.wish01()
Message01.wish02()