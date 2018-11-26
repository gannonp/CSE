# Creating a ;ist
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
