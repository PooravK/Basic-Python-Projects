import random

flag = 1
count = 1
guessed = random.randint(0, 100)

while(flag):
    print("Guess a number between 0 and 100: ", end = "")
    num = int(input())

    if (num > guessed):
        print("Oops! The number is lower than that")
        count = count + 1
    elif (num < guessed):
        print("Oops! The number is greater than that")
        count = count + 1
    else:
        print("Thats the correct number! You guessed the answer in:", count, "turns!")
        break