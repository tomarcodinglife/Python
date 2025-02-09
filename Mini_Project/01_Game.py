import random
# Snake Water Gun Game

computerChoice = random.choice([-1, 0, 1])
myChoice = int(input("Enter Single Number in -1 to 1: "))

dict = {-1 : "Water", 0 : "Gun", 1 : "Snake"}

if(computerChoice == myChoice):
    print(f"Computer Choise = {dict[computerChoice]} and Your Choise= {dict[myChoice]} then Game Draw")
else:
    if(computerChoice == -1 and myChoice == 1):
        print(f"Computer Choise = {dict[computerChoice]} and Your Choise= {dict[myChoice]} then You Win")
    elif(computerChoice == -1 and myChoice == 0):
        print(f"Computer Choise = {dict[computerChoice]} and Your Choise= {dict[myChoice]} then You Loose !")
    elif(computerChoice == 1 and myChoice == -1):
        print(f"Computer Choise = {dict[computerChoice]} and Your Choise= {dict[myChoice]} then You Loose !")
    elif(computerChoice == 1 and myChoice == 0):
        print(f"Computer Choise = {dict[computerChoice]} and Your Choise= {dict[myChoice]} then You Win")
    elif(computerChoice == 0 and myChoice == -1):
        print(f"Computer Choise = {dict[computerChoice]} and Your Choise= {dict[myChoice]} then You Win")
    elif(computerChoice == 0 and myChoice == 1):
        print(f"Computer Choise = {dict[computerChoice]} and Your Choise= {dict[myChoice]} then You Loose")
    else:
        print("Please Input Valid Number")
