name = input("What is your name?")
print('\033[1m' + 'Welcome to my Choose Your Own Adventure game, ' + name + '.' + '\033[0m')
print('\033[1m' + '\033[4m' + "Lets Play!" + '\033[0m')
world_map = {
    'BLUE_STORE': {
        'NAME': "A Blue Store",
        'DESCRIPTION': "This is the store you are in right"
                       " now. There are is a door south, east, west and stairs up north.",
        'PATHS': {
            'UP': 'WARE_HOUSE',
            'SOUTH': 'POLICE_STATION',
            'EAST': 'STREET',
            'WEST': 'REGISTERS'
        }
    },
    'WARE_HOUSE': {
        'NAME': "A Warehouse",
        'DESCRIPTION': "There is some food on the counter.",
        'PATHS': {
            'DOWN': 'BLUE_STORE'
            }
    },
    'STREET': {
        'NAME': "The Streets",
        'DESCRIPTION': "You are on the street and someone is attacking you",
        'PATHS': {
            'WEST': 'BLUE_STORE'
        }
    },
    'REGISTERS': {
        'NAME': "The Registers",
        'DESCRIPTION': "You are next to the registers.",
        'PATHS': {
            'EAST': 'BLUE_STREET'
        }
    },
    'POLICE_STATION': {
        'NAME': "The Police Station",
        'DESCRIPTION': "You are inside the police station and an "
                       "officer is giving you a ride home, go east to get in the car",
        'PATHS': {
            'EAST': 'HOME',
            'SOUTH': 'JAIL',
            'NORTH': 'BLUE_STORE'

        }
    },
    'JAIL': {
        'NAME': "The Jail",
        'DESCRIPTION': "You are in jail and lost all your items and money",
        'PATHS': {
            'NORTH': 'POLICE_STATION'
        }
    },
    'HOME': {
        'NAME': "Outside Home",
        'DESCRIPTION': "You are outside of your house, the door is on the east",
        'PATHS': {
            'EAST': 'INSIDE_HOME'
        }
    },
    'INSIDE_HOME': {
        'NAME': "Inside Home",
        'DESCRIPTION': "You are inside of your house, there is a dark room to the north, a locked room to the east"
                       ", and a kitchen to the south",
        'PATHS': {
            'SOUTH': 'KITCHEN',
            'EAST': 'LOCKED_ROOM',
            'NORTH': 'DARK_ROOM'
        }
    },
    'KITCHEN': {
            'NAME': "The Kitchen",
            'DESCRIPTION': "You are in the kitchen and there is a knife on the counter",
            'PATHS': {
                'SOUTH': 'HOME',
                'NORTH': 'INSIDE_HOME'
            }
    },
    'LOCKED_ROOM': {
        'NAME': "The Locked Room",
        'DESCRIPTION': "You are now inside the locked room.",
        'PATHS': {
            'SOUTH': 'DARK_ROOM2',
            'WEST': 'INSIDE_HOME'
        }
    },
    'DARK_ROOM': {
        'NAME': "The Dark Room",
        'DESCRIPTION': "There is no where to go.",
        'PATHS': {
            'SOUTH': 'INSIDE_HOME'
        }
    },
    'DARK_HALLWAY': {
        'NAME': "The Dark Hallway",
        'DESCRIPTION': "You are inside a dark hallway that stretches West-East.",
        'PATHS': {
            'WEST': 'LOCKED_DOOR',
            'EAST': 'DARK_ROOM2'
        }
    },
    'LOCKED_DOOR': {
        'NAME': "The Locked Door",
        'DESCRIPTION': "There is a locked door and there is a key to open it.",
        'PATHS': {
            'WEST': 'MONEY_ROOM',
            'EAST': 'DARK_HALLWAY'
        }
    },
    'MONEY_ROOM': {
        'NAME': "The Money Room",
        'DESCRIPTION': "There is money everywhere and you need to go back to the store to buy a rifle.",
        'PATHS': {
            'EAST': 'LOCKED_DOOR'
        }
    },
    'CLOSET': {
        'NAME': "The Closet",
        'DESCRIPTION': "You are inside the closet and need to collect the flashlight and key.",
        'PATHS': {
            'NORTH': 'DARK_ROOM2'
        }
    },
    'DARK_ROOM2': {
        'NAME': "The Second Dark Room",
        'DESCRIPTION': "You are inside a pitch black room and to the south is a closet and to the west is a "
                       "dark hallway.",
        'PATHS': {
            'SOUTH': 'CLOSET',
            'WEST': 'DARK_HALLWAY'
        }
    }
}


# print(len(world_map))
playing = True
objects = ['rifle', 'food', 'money', 'flashlight', 'key', 'knife']
current_node = world_map['BLUE_STORE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']

while playing:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input("> ")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node['PATHS'][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("You can't go that way")
    else:
        print("Command Not Found")
    if playing is False:
        print('\033[1m' + '\033[4m' + 'Thank you for playing my Choose Your Own Adventure Game!' + '\033[0m')
        print('\033[1m' + '\033[4m' + 'Have a great day, ' + name + '\033[0m')
