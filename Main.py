from card import card
from Minion import Minion
def main():
    # create the town crier card
    # cost = 1 and name = 'town crier'# 
    # instanciate an object called townCrier
    # creating an instance of the class
    townCrier = Minion(1, "Town Cryer", 1, 2)



    # create an instance of the class called redbandwasp
    redBandWasp = Minion(2, "Redband Wasp", 1, 3)
    #show the player the details of the card
    Warpath = card(2,"Warpath")

   # townCrier.printCardInfo()
    townCrier.printMinionInfo()
    redBandWasp.printMinionInfo()
    Warpath.printCardInfo()


if __name__ == '__main__':
    main()
