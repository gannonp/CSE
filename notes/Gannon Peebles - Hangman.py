import random
import string
print("LETS PLAY HANGMAN!!!")
words = ["ComputeR", "KEYboard"," Mouse", "Computech?", "ClocK", "glasses", "books", "microwave", "flag", "cabinet",
         "CamouflagE"]
guesses = 8
list_of_letters = string.ascii_letters

output = []
word_selection = random.choice(words)
word_list = list(word_selection)
word_list1 = list(word_selection)
length = len(word_selection)
punctuation = string.punctuation
list_of_punctuation = list(punctuation)
print(word_selection)
for i in range(length):
    output.append("* ")

for i in range(length):
    for j in range(len(list_of_punctuation)):
        if list_of_punctuation[j] in word_selection[i]:
            output.pop(i)
            output.insert(i, list_of_punctuation[j])


print("".join(output))
# print(word_list)

while guesses > 0 and len(word_list) > 0:
    user_guess = input("Guess a letter ")
    print('\n' * 10)
    if user_guess.lower() in word_selection or user_guess.upper() in word_selection:
        print("You got it right!")
        for i in range(len(word_selection)):
            if word_selection[i].lower() == user_guess.lower():
                output.pop(i)
                output.insert(i, word_list1[i])
                word_list.pop(i)
        print("".join(output))
    else:
        print("You got it wrong!")
        guesses = (guesses - 1)
        print(guesses)
    if guesses <= 0:
        print("You ran out of guesses. GAME OVER")
    if len(word_list) == 0:
        print("You won!!!")
        print("The word was %s" % word_selection)
