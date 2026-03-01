import random

target = random.randint(1, 100)

while True:
    userChoice = int(input("Guess the target: "))
    if(userChoice == target):
        print("Success : Correct Guess!!")
        break
    elif(userChoice < target):
        print("your number is too small. Take a bigger guess...")
    else:
        print("your number is too big. Take a smaller guess...")    

print("Game is Over!")         