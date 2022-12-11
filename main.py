from Classes import Apples,Cauliflower

objApple = Apples()

print("\n------------ Apple ------------\n")
objApple.setTaste("Sour and Umami")
objApple.setSeeds(5)
print("\n------ Before Consuming -------\n")
objApple.getDetails()
print("\n------ After Consuming --------\n")
objApple.consumeIt()
objApple.getDetails()

objVeg = Cauliflower()

print("\n------------ Cauliflower ------------\n")
objVeg.setTaste("Nutty and Sweet")
objVeg.setLeaves(4)
print("\n------ Before Consuming -------\n")
objVeg.getDetails()
print("\n------ After Consuming --------\n")
objVeg.consumeIt()
objVeg.getDetails()


