states = {
    "CA": "California",
    "FL": "Florida",
    "AK": "Alaska",
    "GA": "Georgia"
}

print(states["CA"])
print(states["AK"])

nested_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000
    },
    "FL": {
        "NAME": "Florida",
        "POPULATION": 21300000
    },
    "AK": {
        "NAME": "Alaska",
        "POPULATION": 737000
    },
    "GA": {
        "NAME": "Georgia",
        "POPULATION": 10500000
    }
}

print(nested_dictionary["GA"]["POPULATION"])
print(nested_dictionary["FL"]["NAME"])

georgia = (nested_dictionary["GA"])
print(georgia)

complex_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000,
        "CITIES": [
            "Fresno",
            "San Francisco",
            "Los Angeles"
        ]
    },
    "FL": {
        "NAME": "Florida",
        "POPULATION": 21300000,
        "CITIES": [
            "Miami",
            "Orlando",
            "Tampa",
            "Jacksonville"
        ]
    },
    "AK": {
        "NAME": "Alaska",
        "POPULATION": 737000,
        "CITIES": [
            "Anchorage",
            "Fairbanks",
            "Juneau"
        ]
    },
    "GA": {
        "NAME": "Georgia",
        "POPULATION": 10500000,
        "CITIES": [
            "Atlanta",
            "Savannah",
            "Augusta"
        ]
    }
}
print(complex_dictionary["AK"]["CITIES"][0])

# Open your notes, and get it to print "Florida"
# And then get it to print "Atlanta" (Because #superbowl)

print(complex_dictionary["FL"])
print(complex_dictionary["GA"]["CITIES"][0])

print(complex_dictionary.keys())
print(complex_dictionary.items())
print(nested_dictionary.items())

for key, value in complex_dictionary.items():
    print(key)
    print(value)
    print("-" * 89)

print()

for state, info in complex_dictionary.items():
    for label, stats in info.items():
        print(label)
        print(stats)
        print("-" * 40)
    print("=" * 40)

# Other notes
states["AR"] = "Arizona?" # It isn't Arizona

print(states["AR"])

states["AR"] = "Arkansas" # Fixed it

print(states["AR"])
