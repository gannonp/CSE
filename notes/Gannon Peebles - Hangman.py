import random
words = ["computer", "keyboard", "mouse", "charger", "clock", "glasses", "books", "school bus"]
guesses = 8
word_selection = random.random(words)

while guesses > 0:
    user = input("Guess a letter")
    if user 