userName = input("Enter username under 10 character: ")

if(len(userName) <= 10):
    print("Your user name is", userName)
else:
    print("Enter Valid username please")