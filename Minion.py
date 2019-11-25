#This class needs to inherit the attributes and behaviors of the card class
# A minion object is a card
# child class == derived class
from card import card
class Minion(card):
    # attribute cost and name
    # inherits cost and name from the parent class card
    def __init__(self, cost, name, damage, health):
        card.__init__(self,cost, name)
        # assign parameters to the object
        self.damage = damage
        self.health = health
    def printMinionInfo(self):
        print ('The card name: ' + str(self.name))
        print ('cost: ' + str(self.cost))
        print('damage: ' + str(self.damage))
        print('health: ' + str(self.health))