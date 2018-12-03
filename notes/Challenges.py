"""
def challenge1(firstname, lastname):
    return (lastname, firstname)
print(challenge1("Gannon", "Peebles"))
"""


def triangle(base, height):
    return(base * height) / 2
print()

print("The area is %s " % triangle(10, 2))
print()

def negative_positive(number):
    return number > 0, number < 0, number == 0


print("The number is positive")
print("The number is negative")
print("The number is zero")
print(negative_positive(41))

