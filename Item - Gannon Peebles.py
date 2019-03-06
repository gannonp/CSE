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


class