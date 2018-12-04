import math
# Challenge 1
def challenge1(first_name, last_name):
    return last_name, first_name


print(challenge1("Gannon", "Peebles"))


# Challenge 2
def triangle(base, height):
    return(base * height) / 2


print()

print("The area is %s " % triangle(10, 2))
print()


# Challenge 3 Easy
def negative_positive(number):
    if number > 0:
        return "The number is positive"
    if number < 0:
        return "The number is negative"
    if number == 0:
        return "The number is zero"


print(negative_positive(41))

# Challenge 5 Medium
print()


def circle_area(radius):
    return math.pi * (radius ** 2)


print("The area of the circle is %s" % circle_area(1.1))
print()


# Challenge 6 Medium


def sphere_volume(radius):
    return (4/3) * math.pi * (radius ** 3)


print("The volume of the sphere is %s" % sphere_volume(5))
