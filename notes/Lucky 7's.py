import random
money = 15
rounds = 0
most = 15

while money >= 1 and money < 30:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    if dice1 + dice2 == 7:
        money += 5
        print("You got 7!")
        print(money)
        print()
        rounds += 1

    if dice1 + dice2 > 7 or dice1 + dice2 < 7:
        print("You did not get seven")
        money -= 1
        print(money)
        print("You rolled a")
        print(dice1 and dice2)
        print()
        rounds += 1
    if money > most:
        most = money

print("You played")
print(rounds)
print("rounds")
print()
print("Your most amount of money was")
print(most)
