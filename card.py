#card class is a blueprint of the card object
class card:

    #initializer to create the attributes of every class object
    # constructor 
    # parent class -- base class
    def __init__(self,cost,name):
        self.cost = cost
        self.name = name
        #attributes describe the object = argument parameter
        # give the card a cost attribute
        # give the card a name attricute
    def printCardInfo(self):
        print ('The card name: ' + str(self.name))
        print ('cost: ' + str(self.cost))




# behaviors - methods - functions