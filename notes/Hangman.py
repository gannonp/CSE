import random
word = ["computer", "keyboard", "mouse", "charger", "clock"]
print(random.choice(word))
turns = 10

while turns >= 1:
    guess = input("Guess a letter")
    if guess == word:
        print("You got a letter correct!")
        turns =- 5
    else:
        print("You got it wrong")