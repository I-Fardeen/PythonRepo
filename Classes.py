class Edibles:
    state = "isEdible"
    __isconsumed = False
    def consume(self,isconsumed):
        self.__isconsumed = isconsumed
    def getConsumedState(self):
        return self.__isconsumed
    def hasTaste(self,tastetype):
        self.tastetype = tastetype
    
class Fruits(Edibles):
    state = "isFruit"
    def hasSeeds(self,nseeds):
        self.nseeds = nseeds

class Vegetables(Edibles):
    state = "isVegetable"
    def hasLeaves(self,nleaves):
        self.leaves = nleaves

class Apples(Fruits):
    def __init__(self):
        self.gstate = Edibles.state
        self.pstate = Fruits.state
    def setTaste(self,taste):
        self.hasTaste(taste)
    def setSeeds(self,seeds):
        self.hasSeeds(seeds)
    def consumeIt(self):
        self.consume(True)
    def getDetails(self):
        print("General state: {}".format(self.gstate))
        print("Specific state: {}".format(self.pstate))
        print("Taste: {}".format(self.tastetype))
        print("No. of Seeds: {}".format(self.nseeds))
        print("Is Consumed: {}".format(self.getConsumedState()))

class Cauliflower(Vegetables):
    def __init__(self):
        self.gstate = Edibles.state
        self.pstate = Vegetables.state
    def setTaste(self,taste):
        self.hasTaste(taste)
    def setLeaves(self,leaves):
        self.hasLeaves(leaves)
    def consumeIt(self):
        self.consume(True)
    def getDetails(self):
        print("General state: {}".format(self.gstate))
        print("Specific state: {}".format(self.pstate))
        print("Taste: {}".format(self.tastetype))
        print("No. of Leaves: {}".format(self.leaves))
        print("Is Consumed: {}".format(self.getConsumedState()))
    
