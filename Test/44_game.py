import random

# yourScore = int(input("Enter Your Number from 0 to 50: "))
# computerScore = random.randint(0, 50)

file = open("C:/Users/PC/OneDrive/Documents/Python/Test/45_Gamefile.txt")

def game():
    print("You Are Playing Game")
    score = random.randint(0, 50)
    highScore = file.read()
    if(highScore != ""):
        highScore = int(highScore)
    else:
        highScore = 0

    print(f"Your Score {score}")
    if(score > highScore):
        with open ("C:/Users/PC/OneDrive/Documents/Python/Test/45_Gamefile.txt", "w") as f:
            f.write(str(score))
    
    return score

game()



