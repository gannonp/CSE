import random
money = 15

while money >= 1 and money < 30:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    if dice1 + dice2 == 7:
        money += 5
        print("You got 7!")
        print(money)
        print()
    if dice1 + dice2 > 7 or dice1 + dice2 < 7:
        print("You did not get seven")
        money -= 1
        print(money)
        print("You rolled a")
        print(dice1 and dice2)
        print()
