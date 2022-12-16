#Rock Paper Scissors Game

Author: Fardeen Ahmad Khan

Hi there! This project is a simple python program that simulates the famous RPS Game. This directory contains two files:

        - RockPaperSci.py: contains the two classes Player and Computer, Player has attributes 'lives', 'score', 'choice' all of these are accessed by custom getters and setters. All these are manipulated by game logic.

        - main.py: This is the main file which has the gameStart function, inside the function is the real comparison which determines the winner and loser and call the appropriate function to update the values for the player.

##Game Rules


1. If the player and computers have same choice it's a tie and no updation to any values.

2. If the Player wins, his score is updated by 100.

3. If the Player loses, his lives are deducted by 1.

4. Computer's values are chosen by a random function.

5. If the player loses all lives the game ends.

Hope you enjoy the game!