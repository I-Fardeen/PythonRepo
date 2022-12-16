#Author: Fardeen Ahmad Khan
from random import randint
choices=["Rock","Paper","Scissors"]

class Player:
    _lives = 0
    _choice = ""
    _score = 0
    def __init__(self) -> None:
        self._lives = 3
        self._score = 0
    def setChoice(self,i):
        self._choice = choices[i]
    def getChoice(self):
        return self._choice
    def getScore(self):
        return self._score
    def getLives(self):
        return self._lives
    def playerLost(self):
        self._lives = self._lives - 1
    def playerWon(self):
        self._score = self._score + 100

class Computer:
    _choice=""
    def setChoice(self):
        self._choice = choices[randint(0,2)]
    def getChoice(self):
        return self._choice