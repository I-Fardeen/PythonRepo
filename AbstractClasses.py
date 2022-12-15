#Author: Fardeen Ahmad Khan
#Email: fardeenahmadkhan786@gmail.com
import abc
from abc import ABC, abstractmethod

#region Abstract Class Machine
class Machine(ABC):
    _mId = ""
    @abstractmethod
    def getMachineId(self): pass
    @abstractmethod
    def setMachineId(self,mid): pass
#endregion

#region Child Class Laptop Inherits Machine
class Laptop(Machine):
    def setMachineId(self,mid): 
        self._mId = mid
    def getMachineId(self): 
        return self._mId
    def setLaptopId(self,lid):
        self._lid = lid
    def getLaptopId(self): 
        return self._lid
    def getDetails(self):
        print("\n-----------Laptop-----------")
        print("Machine Id: {}".format(self.getMachineId()))
        print("Laptop Id: {}".format(self.getLaptopId()))
        print("-----------XXXXXX-----------\n")
#endregion

#region Child Class Printer Inherits Machine
class Printer(Machine):
    def setMachineId(self, mid):
        self._mId = mid
    def getMachineId(self):
        return self._mId
    def setPrinterId(self,pid):
        self._pid = pid
    def getPrinterId(self):
        return self._pid
    def getDetails(self):
        print("\n-----------Printer----------")
        print("Machine Id: {}".format(self.getMachineId()))
        print("Laptop Id: {}".format(self.getPrinterId()))
        print("-----------XXXXXX-----------\n")
#endregion

lp = Laptop()
pt = Printer()

#region Driver Code
print("\nHi there! Please choose one of the devices")
inp = input("Enter 1 for Laptop and 2 for Printer")
if(int(inp) == 1):
    mid = input("\nPlease Enter Machine Number for your Laptop")
    lp.setMachineId(mid)
    lid = input("\nPlease Enter Laptop Number for your Laptop")
    lp.setLaptopId(lid)
    print("\nDisplaying the details")
    lp.getDetails()

elif(int(inp)==2):
    mid = input("\nPlease Enter Machine Number for your Printer")
    pt.setMachineId(mid)
    pid = input("\nPlease Enter Printer Number for your Printer")
    pt.setPrinterId(pid)
    print("\nDisplaying the details")
    pt.getDetails()

else:
    print("Please choose a correct option!")

#endregion