class Item(object):
    def __init__(self, name):
        self.name = name


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

    def consume(self, player, consumable):
        player.health += consumable.health_added
        if self.health <= 0:
            player.health = 0
        print("%s consumed %s and %s now has %d health" % (self.name, consumable.name, player.name, player.health))
        if self.health <= 0:
            print("You died")
            return
        if self.health >= 500:
            player.health = 500
            print("%s has max health, 500!" % player.name)


orc = Character("Orc", 100, Scar())
demon = Character("Demon", 300, Revolver())

orc.consume(orc, GoldenApple())
orc.attack(demon)
demon.attack(orc)
demon.attack(orc)
orc.attack(demon)
demon.consume(demon, GoldenApple())
orc.consume(orc, HealthPotion())
