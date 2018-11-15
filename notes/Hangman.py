import random
word = ['computer', 'keyboard', 'mouse', 'charger', 'clock']
random
turns = 10

while turns >= 1:
    guess = input("Guess a letter")
    if guess == word:
        print("You got a letter correct!")