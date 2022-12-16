#Author: Fardeen Ahmad Khan
from RockPaperSci import Player,Computer
ch = 1
def gameStart():
    plr = Player()
    cmp = Computer()
    print("\n ------ Game Start ------")
    while plr.getLives() >= 0:
        print("\n------------------------------------------------------")
        print("\nReady Player? You have {} lives".format(plr.getLives()))
        print("\nYour current score: {}".format(plr.getScore()))
        print("\nEnter '1' for Rock '2' for Paper '3' for Scissors")
        print("\nEnter '0' to go back to Main Screen")
        print("\n------------------------------------------------------")
        inp = input("\nEnter your choice: ")

        cmp.setChoice()
        if(int(inp)==1):
            plr.setChoice(0)
            if(plr.getChoice()==cmp.getChoice()):
                print("\nIt's a Tie!")
                continue
            elif(cmp.getChoice()=="Paper"):
                print("\n You lose! Paper covers Rock...")
                plr.playerLost()
                continue
            elif(cmp.getChoice()=="Scissors"):
                print("\n You Win! Rock crushes Scissors...")
                plr.playerWon()
                continue
        elif(int(inp)==2):
            plr.setChoice(1)
            if(plr.getChoice()==cmp.getChoice()):
                print("\nIt's a Tie!")
                continue
            elif(cmp.getChoice()=="Scissors"):
                print("\n You lose! Scissors cut Paper...")
                plr.playerLost()
                continue
            elif(cmp.getChoice()=="Rock"):
                print("\n You Win! Paper covers Rock...")
                plr.playerWon()
                continue
        elif(int(inp)==3):
            plr.setChoice(2)
            if(plr.getChoice()==cmp.getChoice()):
                print("\nIt's a Tie!")
                continue
            elif(cmp.getChoice()=="Rock"):
                print("\n You lose! Rock crushes Scissors...")
                plr.playerLost()
                continue
            elif(cmp.getChoice()=="Paper"):
                print("\n You Win! Scissors cut Paper...")
                plr.playerWon()
                continue
        elif(int(inp)==0):
            return
        else:
            print("Please enter a valid choice!")
            continue
    print("\n ------ Game Ended ------")
    print("\n Your final score is: {}".format(plr.getScore()))

while(ch!=0):
    print("\nWelcome to the Rock, Paper, Scissors game!")
    print("\nPress 1 to Start the Game | Press 0 to Exit")
    ch = int(input("\n Your choice: "))
    if(ch==1):
        gameStart()
    elif(ch==0):
        print("Exiting the Game!")
        exit(0)
    else:
        print("Please enter a valid choice!")




                

