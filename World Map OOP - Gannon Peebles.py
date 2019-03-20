class Room(object):
    def __init__(self, name, north, south, east, west, up, down, description, item=None):
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.name = name
        self.description = description
        self.characters = []
        self.item = item


class Item(object):
    def __init__(self, name):
        self.name = name


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

    def consume(self, consumable):
        player.health += consumable.health_added
        if self.health <= 0:
            player.health = 0
        print("%s consumed %s and %s now has %d health" % (player, consumable.name, player, self.health))
        if self.health <= 0:
            print("You died")
            return
        if self.health >= 500:
            player.health = 500
            print("%s has max health, 500!" % player)


class Demon(object):
    def __init__(self, health):
        self.health = health
        self.inventory = []

    def hurt_player(self, health):
        self.health = health
        if self.health <= 0:
            print("You died")
            return


class Melee(Item):
    def __init__(self, name, damage, durability):
        super(Melee, self).__init__(name)
        self.damage = damage
        self.durability = durability


class Gun(Item):
    def __init__(self, name, damage, ammo):
        super(Gun, self).__init__(name)
        self.safety_mode = True
        self.damage = damage
        self.ammo = ammo

    def turn_off_safety_mode(self):
        self.safety_mode = False
        print("You turned off the safety mode")

    def shoot_(self):
        self.ammo -= 10
        print("You shot the gun")


class Pistol(Gun):
    def __init__(self, name, damage, ammo):
        super(Pistol, self).__init__(name, damage, ammo)


class AssaultRifle(Gun):
    def __init__(self, name, damage, ammo):
        super(AssaultRifle, self).__init__(name, damage, ammo)


class AK47(AssaultRifle):
    def __init__(self):
        super(AK47, self).__init__("AK47", 35, 200)


class Scar(AssaultRifle):
    def __init__(self):
        super(Scar, self).__init__("Scar", 50, 180)


class Burst(AssaultRifle):
    def __init__(self):
        super(Burst, self).__init__("Burst", 35, 120)


class Revolver(Pistol):
    def __init__(self):
        super(Revolver, self).__init__("Revolver", 70, 30)


class Consumable(Item):
    def __init__(self, name, health_added):
        super(Consumable, self).__init__(name)
        self.health_added = health_added


class HealthPotion(Consumable):
    def __init__(self):
        super(HealthPotion, self).__init__("Health Potion", 75)


class Apple(Consumable):
    def __init__(self):
        super(Apple, self).__init__("Apple", 10)


class GoldenApple(Consumable):
    def __init__(self):
        super(GoldenApple, self).__init__("Golden Apple", 200)


class PoisonBerry(Consumable):
    def __init__(self):
        super(PoisonBerry, self).__init__("Berry", -30)


class HealthyBerry(Consumable):
    def __init__(self):
        super(HealthyBerry, self).__init__("Berry", 15)


class RatPoison(Consumable):
    def __init__(self):
        super(RatPoison, self).__init__("Rat Poison", -300)


class DeathPotion(Consumable):
    def __init__(self):
        super(DeathPotion, self).__init__("Death Potion", -1000)


class Animal(Item):
    def __init__(self, name):
        super(Animal, self).__init__(name)


class CrazyDog(Animal):
    def __init__(self):
        super(CrazyDog, self).__init__("Crazy Dog")


class GoldenUnicorn(Animal):
    def __init__(self):
        super(GoldenUnicorn, self).__init__("Golden Unicorn")


class GiantBird(Animal):
    def __init__(self):
        super(GiantBird, self).__init__("Giant Bird")


class Technology(Item):
    def __init__(self, name):
        super(Technology, self).__init__(name)


class Computer(Technology):
    def __init__(self):
        super(Computer, self).__init__("Computer")


class Phone(Technology):
    def __init__(self):
        super(Phone, self).__init__("Phone")


class Character(object):
    def __init__(self, name, health: int, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon

    def take_damage(self, damage: int):
        self.health -= damage
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)

    def consume(self, consumable):
        player.health += consumable.health_added
        if self.health <= 0:
            player.health = 0
        print("%s consumed %s and %s now has %d health" % (self.name, consumable.name, self.name, self.health))
        if self.health <= 0:
            print("You died")
            return
        if self.health >= 500:
            player.health = 500
            print("%s has max health, 500!" % player)


revolver = Revolver()
ak47 = AK47()
scar = Scar()
burst = Burst()
health_potion = HealthPotion()
apple = Apple()
golden_apple = GoldenApple()
poison_berry = PoisonBerry()
healthy_berry = HealthyBerry()
rat_poison = RatPoison()
death_potion = DeathPotion()
crazy_dog = CrazyDog()
golden_unicorn = GoldenUnicorn()
giant_bird = GiantBird()
computer = Computer()
phone = Phone()
blue_gold_fish = Character("Blue Goldfish", 100, Burst)
demon = Character("Demon", 300, Revolver)

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
                                                                                                           "north.",
                  phone)
ware_house = Room('The Ware House', None, None, None, None, None, 'blue_store', "There is some food on the counter.",
                  apple)
street = Room('The Street', None, None, None, 'blue_store', None, None, "You are on the street and someone is "
                                                                        "attacking you", death_potion)
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
    elif "consume" in command:
        player.consume(self.item)
    else:
        print("Command Not Found")
    if not playing:
        break
