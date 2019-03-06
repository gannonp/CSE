class Playstation4(object):
    def __init__(self, number_of_games, internet, money):
        self.controller = True
        self.disk = True
        self.power = True
        self.hdmi = True
        self.number_of_games = number_of_games
        self.headset = True
        self.internet = internet
        self.wallet = money
        self.headset_charge = 100

    def buy_game(self, cost):
        if not self.power:
            print("Your PS4 has no power.")
            return
        if not self.internet:
            print("You have no internet to buy the game.")
            return
        if not self.hdmi:
            print("Your PS4 is not connected to a TV or monitor.")
            return
        if not self.controller:
            print("You have no controller to buy the game with.")
            return
        self.wallet -= cost
        if self.wallet < cost:
            print("You don't have enough money.")
            return
        else:
            print("You bought the game successfully.")

    def play(self, game_age_rating):
        if not self.power:
            print("Your PS4 has no power.")
            return
        if not self.internet:
            print("You have no internet to play with.")
            return
        if not self.hdmi:
            print("Your PS4 is not connected to a TV or monitor.")
            return
        if not self.controller:
            print("You have no controller to play with")
            return
        if self.number_of_games <= 0:
            print("You have no games to play")
            return
        if self.internet == "Cox" or self.internet == "AT&T":
            print("You internet is horrible and you cannot play")
            return
        if game_age_rating >= 18:
            print("You are not old enough to play this game.")
            return
        if game_age_rating < 18:
            print("You are playing the game")

    def talk(self, duration):
        if not self.power:
            print("Your PS4 has no power.")
            return
        if not self.internet:
            print("You have no internet to play with.")
            return
        if not self.hdmi:
            print("Your PS4 is not connected to a TV or monitor.")
            return
        if not self.controller:
            print("You have no controller to play with.")
            return
        if not self.headset:
            print("You have no headset to play with.")
            return
        if self.headset_charge <= 0:
            print("Your headset is dead.")
            return
        battery_loss_per_minute = 1
        self.headset_charge -= duration * battery_loss_per_minute
        if self.headset_charge < 0:
            self.headset_charge = 0
            print("Your headset died while you were talking in the party.")
        elif self.headset_charge == 0:
            print("Your phone died at the end of the conversation.")
        else:
            print("Your headset did not die and is at %s charge" % self.headset_charge)

    def unplug_power(self):
        print("You unplugged the power cable")
        self.power = False

    def unplug_hdmi(self):
        print("You unplugged the HDMI cable from the PS4 to the TV.")
        self.hdmi = False

    def break_controller(self):
        print("You broke your controller.")
        self.controller = False


new_ps4 = Playstation4(10, "Comcast", 100)
new_ps4.play(40)
print()
old_ps4 = Playstation4(10, "AT&T", 50)
old_ps4.unplug_power()
old_ps4.play(15)
print()
new_ps4.unplug_hdmi()
new_ps4.buy_game(40)
print()
your_ps4 = Playstation4(50, "T-Mobile", 100)
your_ps4.break_controller()
your_ps4.play(10)
