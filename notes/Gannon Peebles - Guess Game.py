import random
attempts = 1
number = random.randint(1,10)
isCorrect = False

guess = int(input("Guess a number between 1 and 10. "))

while number != guess and attempts < 5:
    if guess < number:
        print("Higher")
    elif guess > number:
        print("Lower")
    guess = int(input("Take a guess."))
    attempts += 1

if attempts == 5:
    print("You ran out of tries")
    print("The correct number was %d" % number)

else:
    print("You got it right!")
    print("You got it right in %d attempts" % attempts)