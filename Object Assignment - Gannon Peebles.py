class Playstation4(object):
    def __init__(self, number_of_games, money):
        # These are attributes that a phone has.
        # These should all be relevant to our program
        self.power = True
        self.headset = True
        self.number_of_games = number_of_games
        self.wallet = money
        self.controller = True
        self.hdmi = True
        self.controller_charge = 100
        self.headset_charge = 100

    def play(self, game_age_rating):
        if not self.power:
            print("You don't have power.")
            return
        if not self.hdmi:
            print("You don't have a TV to play on.")
            return
        if not self.controller:
            print("You don't have a controller")
            return
        if self.controller_charge <= 0:
            print("Your controller is dead.")
            return
        if game_age_rating >= 18:
            print("You are not old enough to play.")
            return
        else:
            print("You are successfully playing the game.")

    def break_power(self):
        self.power = False

    def break_hdmi(self):
        self.hdmi = False

    def buy_game(self, cost, game_age_rating):
        if not self.power:
            print("You don't have power.")
            return
        if not self.hdmi:
            print("You don't have a TV to play on.")
            return
        if not self.controller:
            print("You don't have a controller")
            return
        if self.controller_charge <= 0:
            print("Your controller is dead.")
            return
        if game_age_rating >= 18:
            print("You are not old enough to play.")
            return
        if cost > self.wallet:
            print("You don't have enough money.")
            return
        else:
            print("You bought the game.")

    def talk_in_party(self, duration):
        charge_loss_per_minute = 5
        if not self.power:
            print("You don't have power.")
            return
        if not self.hdmi:
            print("You don't have a TV to play on.")
            return
        if not self.controller:
            print("You don't have a controller")
            return
        if self.controller_charge <= 0:
            print("Your controller is dead.")
            return
        if not self.headset:
            print("You don't have a headset to talk with")
            return
        if self.headset_charge <= 0:
            print("Your headset is dead.")
        self.headset_charge -= duration * charge_loss_per_minute
        if self.headset_charge < 0:
            self.headset_charge = 0
            print("Your headset died while you were in the party.")
        elif self.headset_charge == 0:
            print("Your headset died when you finished playing.")
        else:
            print("You talked in the party and your headset did not die.")
            print("Your headset is currently at %s and you can talk for %d "
                  "minutes longer" % (self.headset_charge, self.headset_charge/5))


your_ps4 = Playstation4(10, 100)
your_ps4.talk_in_party(10)
