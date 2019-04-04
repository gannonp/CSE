class Room(object):
    def __init__(self, name, north, south, east, west, up, down, description, item=None, animal=None):
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
        self.enemy = []
        self.animal = animal


class Item(object):
    def __init__(self, name):
        self.name = name


class Player(object):
    def __init__(self, starting_location, weapon=None):
        self.current_location = starting_location
        self.inventory = []
        self.health = 100
        self.name = "you"
        self.weapon = weapon

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
        print("%s consumed %s and %s now have %d health" % (player.name, consumable.name, player.name, self.health))
        if self.health <= 0:
            print("You died")
            return
        if self.health >= 500:
            player.health = 500
            print("%s has max health, 500!" % player)

    def take_damage(self, damage: int):
        self.health -= damage
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (player.name, target.name, player.weapon.damage))
        target.take_damage(self.weapon.damage)

    def turn_on(self):
        print("Your player turned on the flashlight and it gave you extra vision, you got 5 health added.")
        player.health += 5

    def turn_off(self):
        print("Your player turned off the flashlight and it took your extra vision, you lost 5 health.")
        player.health -= 5


class Demon(object):
    def __init__(self, health):
        self.health = health
        self.inventory = []

    def hurt_player(self, health):
        self.health = health
        if self.health <= 0:
            print("You died")
            return

    def take_damage(self, damage: int):
        self.health -= damage
        print("The demon has %d health left" % self.health)
        if self.health <= 0:
            print("The demon died")
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

    def take_damage(self):
        self.health -= player.weapon.damage
        print("%s has %d health left" % (self.name, self.health))

    def attack(self, target):
        print("%s attacks %s for %d damage" % (self.name, target.name, self.weapon.damage))
        target.take_damage(self.weapon.damage)

    def consume(self, consumable):
        player.health += consumable.health_added
        if self.health <= 0:
            player.health = 0
        print("%s consumed %s and %s now has %d health" % (self.name.upper(), consumable.name, self.name, self.health))
        if self.health <= 0:
            print("You died")
            return
        if self.health >= 500:
            player.health = 500
            print("%s has max health, 500!" % player)


class Hands(Melee):
    def __init__(self):
        super(Hands, self).__init__("Hands", 20, 100)


class Flashlight(Item):
    def __init__(self):
        super(Flashlight, self).__init__("Flashlight")


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
flashlight = Flashlight()

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
registers = Room('The Registers', None, None, 'blue_store', None, None, None, "You are next to the registers.",
                 golden_unicorn)
police_station = Room('The Police Station', 'blue_store', 'jail', 'outside_home', None, None, None, "You are inside "
                                                                                                    "the "
                                                                                                    "police station "
                                                                                                    "and an "
                                                                                                    "officer is giving "
                                                                                                    "you a ride home, "
                                                                                                    "go east to get in "
                                                                                                    "the car",
                      healthy_berry)
jail = Room('The Jail', 'police_station', None, None, None, None, None, "You are in jail and lost all your items "
                                                                        "and money", rat_poison)
outside_home = Room('Outside The House', None, None, 'inside_home', None, None, None, "You are outside of your house, "
                                                                                      "the door is on the east",
                    crazy_dog)
inside_home = Room('Inside The House', 'dark_room', 'kitchen', 'unlocked_room', None, None, None, "You are inside of "
                                                                                                  "your house, "
                                                                                                  "there is a dark"
                                                                                                  " room "
                                                                                                  "to "
                                                                                                  "the north, a "
                                                                                                  "locked room "
                                                                                                  "to the east"
                                                                                                  ", and a kitchen to "
                                                                                                  "the south",
                   blue_gold_fish)
kitchen = Room('The Kitchen', 'inside_home', 'outside_home', None, None, None, None, "You are in the kitchen and there "
                                                                                     "is a burst on the counter", burst)
unlocked_room = Room('The Locked Room', None, 'dark_room_2', None, 'inside_home', None, None, "You are now inside the "
                                                                                              "unlocked room.")
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
                                                                                 "store to buy a rifle.", phone)
closet = Room('The Closet', None, 'blue_store', None, None, None, None, "You are inside the closet.", flashlight)
dark_room_2 = Room('The Second Dark Room', None, None, None, 'dark_hallway', None, None, "You are inside a pitch black "
                                                                                         "room and to the west is a "
                                                                                         "dark hallway.", ak47)

player = Player(blue_store)

playing = True
directions = ['north', 'south', 'east', 'west', 'up', 'down']
deal_damage = True

while playing:
    if deal_damage:
        print('\033[4m' + "A demon is always following you, he has 300 health, he only attacks when you "
              "enter the wrong room, "
              "he deals "
              "25 damage each time" + '\033[1m')
    deal_damage = False
    print(player.current_location.name)
    print(player.current_location.description)
    if player.current_location.item is not None:
        print("There is a %s here." % player.current_location.item.name.lower())
    if player.current_location.animal is not None:
        print("There is a %s here." % player.current_location.animal.name.lower())
    command = input("> ")
    if player.current_location.item is not None and ('pick up' in command.lower() or 'grab' in command.lower()):
        try:
            player.inventory.append(player.current_location.item.name)
            print("Your player picked up the %s" % player.current_location.item.name.lower())
            player.current_location.item = None
        except AttributeError:
            print("You cannot pick this up")
            pass
    if flashlight in player.inventory and ('turn on' in command.lower() or 'flip on' in command.lower()):
            player.turn_on()
            print("Your player turned on the %s" % player.current_location.item.name.lower())
            player.current_location.item = None
    if flashlight not in player.inventory and ('turn on' in command.lower() or 'flip on' in command.lower()):
        print("You don't have a flashlight")
        pass
    elif command.lower() in ['q', 'quit', 'exit']:
        playing = False
    elif command.lower() in ['i', 'inventory']:
        print("Your current inventory is:")
        print(list(player.inventory))
    elif command.lower() in ['a', 'attack', 'fight', 'kill']:
        try:
            player.weapon = Hands()
            demon.take_damage()
        except AttributeError:
            print("There is no one to attack")
    elif command.lower() in directions:
        try:
            next_room = player.find_next_room(command.lower())
            player.move(next_room)
        except KeyError:
            print("I can't go that way")
    elif 'consume' in command or 'eat' in command:
        try:
            player.consume(player.current_location.item)
            player.current_location.item = None
        except AttributeError:
            pass
        print("Command Not Found")
    if not playing:
        break
    if player.health <= 0:
        print("You died")
        break
    if player.current_location == street:
        print("There is a hobo attacking you")
        print("You died")
        break
