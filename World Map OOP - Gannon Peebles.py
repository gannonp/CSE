class Room(object):
    def __init__(self, name, north, south, east, west, up, down, description):
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.name = name
        self.description = description
        self.characters = []


class Player(object):
    def __init__(self, starting_location):
        self.current_location = starting_location
        self.inventory = []
        self.health = 100

    def move(self, new_location):
        # This moves the player the player to a new room
        """

       :param new_location: The room object of which you are going to
        """
        self.current_location = new_location

    def find_next_room(self, direction):
        """ This method searches the current room so see if  a room exists in that direction.

        :param direction: The direction that you want to move to
        :return: The Room object if it exists, or None if it does not
        """
        name_of_room = getattr(self.current_location, direction)
        return globals()[name_of_room]


class Demon(object):
    def __init__(self, health):
        self.health = health
        self.inventory = []

    def hurt_player(self, health):
        self.health = health
        if self.health <= 0:
            print("You died")
            return


blue_store = Room('The Blue Store', 'closet', 'police_station', 'street', 'registers', 'ware_house', None, "This is "
                                                                                                           "the "
                                                                                                           "store you "
                                                                                                           "are"
                                                                                                           " in "
                                                                                                           "right" " "
                                                                                                           "now. There "
                                                                                                           "are is a "
                                                                                                           "door "
                                                                                                           "south, "
                                                                                                           "east, "
                                                                                                           "west and "
                                                                                                           "stairs up "
                                                                                                           "north.")
ware_house = Room('The Ware House', None, None, None, None, None, 'blue_store', "There is some food on the counter.")
street = Room('The Street', None, None, None, 'blue_store', None, None, "You are on the street and someone is "
                                                                        "attacking you")
registers = Room('The Registers', None, None, 'blue_store', None, None, None, "You are next to the registers.")
police_station = Room('The Police Station', 'blue_store', 'jail', 'outside_home', None, None, None, "You are inside "
                                                                                                    "the "
                                                                                                    "police station "
                                                                                                    "and an "
                                                                                                    "officer is giving "
                                                                                                    "you a ride home, "
                                                                                                    "go east to get in "
                                                                                                    "the car")
jail = Room('The Jail', 'police_station', None, None, None, None, None, "You are in jail and lost all your items "
                                                                        "and money")
outside_home = Room('Outside The House', None, None, 'inside_home', None, None, None, "You are outside of your house, "
                                                                                      "the door is on the east")
inside_home = Room('Inside The House', 'dark_room', 'kitchen', 'locked_room', None, None, None, "You are inside of "
                                                                                                "your house, "
                                                                                                "there is a dark room "
                                                                                                "to "
                                                                                                "the north, a "
                                                                                                "locked room "
                                                                                                "to the east"
                                                                                                ", and a kitchen to "
                                                                                                "the south")
kitchen = Room('The Kitchen', 'inside_home', 'outside_home', None, None, None, None, "You are in the kitchen and there "
                                                                                     "is a knife on the counter")
locked_room = Room('The Locked Room', None, 'dark_room_2', None, 'inside_home', None, None, "You are now inside the "
                                                                                            "locked room.")
dark_room = Room('The Dark Room', None, 'inside_home', None, None, None, None, "There is no where to go.")
dark_hallway = Room('The Dark Hallway', None, None, 'dark_room_2', 'locked_door', None, None, "You are inside a dark "
                                                                                              "hallway that stretches "
                                                                                              "West-East.")
locked_door = Room('The Locked Door', None, None, 'dark_hallway', 'money_room', None, None, "There is a locked door "
                                                                                            "and "
                                                                                            "there is a key to open "
                                                                                            "it.")
money_room = Room('The Money Room', None, None, 'locked_door', None, None, None, "There is money everywhere and you "
                                                                                 "need to go back to the "
                                                                                 "store to buy a rifle.")
closet = Room('The Closet', None, 'blue_store', None, None, None, None, "You are inside the closet and "
                                                                        "need to collect the flashlight and key.")
dark_room_2 = Room('The Second Dark Room', None, None, None, 'dark_hallway', None, None, "You are inside a pitch black "
                                                                                         "room and to the west is a "
                                                                                         "dark hallway.")

player = Player(blue_store)
demon = Demon(100)
street.characters.append(demon)


playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']

while playing:
    print(player.current_location.name)
    print(player.current_location.description)
    command = input("> ")
    if command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command.lower())
            player.move(next_room)
        except KeyError:
            print("I can't go that way")
    else:
        print("Command Not Found")
    if not playing:
        break
