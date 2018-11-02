import random
number = random.randint(1,1)

guess = int(input("Guess a number between 1 and 10. "))
while number == guess:
    print("Correct")