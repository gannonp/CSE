"""
# Creating a list
colors = ["blue", "turquoise", "pink", "orange", "black", "red", "lemon", "green", "brown"]  # Use sqaure brackets !!!!
print(colors)
print(colors[0])
print(colors[1])

# Length of the list
print("There are %d things in the ;ost." % len(colors))

# Changing Elements in a list
colors[1] = "purple"
print(colors)

# Looping through lists
for item in colors:
    print(item)

print()
'''
1. Make a list
2. Change the 3rd thing in the list
3. Print the item
4. Printhe full list
'''

dogs = ["pitbull", "dogo argentino", "pug", "boxer", "german shepard", "bulldog", "golden retriever", "puma"]
dogs[2] = "shitzu"
print(dogs[2])
print(dogs)
for item in dogs:
    print(item)
print("The last thing in the list is the %s" % dogs[len(dogs) - 1])

# Slicing a list
print(dogs[1:3])
print()
"""

food_list = ["pie", "apple", "banana", "tamales", "tacos", "pizza", "burrito", "sushi", "peanut butter", "bacon", "noodles", "chicken", "chili", "chips", "hot wings", "fettuccine", "carne asada", "salad", "poutine"]
print(len(food_list))

# Adding stuff to a list
food_list.append("eggs")
food_list.append("sausage")
# Notice that everything is oject.method(parameters)
print(food_list)

food_list.insert(1, "eggo waffles")
print(food_list)

# Removing things from a list
food_list.remove("salad")
print(food_list)
print()
print()

shoes = ["Jordan", "Adidas", "Nike"]
shoes.remove("Jordan")
shoes.append("Vans")
print(shoes)

# Tuples
brands = ("apple", "samsung", "HTC")  # Notice the parentheses

# Also removing stuff from a list
print(food_list)
food_list.pop(0)
print(food_list)


# Find the index of an item
print(food_list.index("chicken"))

# Changing things into a list
string1 = "turquoise"
list1 = list(string1)
print(list1)

# Hangman Hints
for i in range(len(list1)):  # i goees through all indicies
    if list1[i] == "u": # if we find a U
        list1.pop(i)  # Reomve i-th index
        list1.insert(i, "*")  # Put a * there instead
'''
for character in list1:
    if character == "u":
    # replace with a *
    current_index = list1.index(character)
    list1.pop(current_index)
    list1.insert(current_index, "*")
'''
# Turn a list into a string
print("".join(list1))

# Function Notes
# a**2 + b**2 = c**2


def pythagorean(a, b):
    return (a**2 + b**2)**(1/2)


print(pythagorean(3, 4))
