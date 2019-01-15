import random
import string
print("LETS PLAY HANGMAN!!!")
words = ["computer", "keyboard", "mouse", "charger", "clock", "glasses", "books", "microwave", "flag", "camera"]
guesses = 8
list_of_letters = string.ascii_letters

output = []
word_selection = random.choice(words)
word_list = list(word_selection)
length = len(word_selection)
print(word_selection)
for i in range(length):
    output.append("_ ")
print("".join(output))
# print(word_list)

while guesses > 0 and len(word_list) > 0:
    user_guess = input("Guess a letter")
    if user_guess in word_selection:
        print("You got it right!")
        word_list.remove(user_guess)
    else:
        print("You got it wrong!")
        guesses = (guesses - 1)
        print(guesses)
    if guesses <= 0:
        print("You ran out of guesses. GAME OVER")
    if len(word_list) == 0:
        print("You won!!!")




